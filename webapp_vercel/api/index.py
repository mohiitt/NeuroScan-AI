"""
Alzheimer's Disease Detection - FastAPI Backend
Serves feature extraction and XGBoost inference for the Phase 2 pipeline.
(Lightweight Vercel version: Pure Python, zero ML dependencies)
"""

import json
import logging
from pathlib import Path

from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Hardcoded config — paths relative to api directory
# ---------------------------------------------------------------------------
API_ROOT = Path(__file__).parent
DATA_JSON = API_ROOT / "data" / "patient_data.json"
DEFAULT_SESSION = "OAS1_0003_MR1"

# Full-feature mode
MODES = {
    "full": {
        "data_dir":   API_ROOT / "data" / "data_full",
        "models_dir": API_ROOT / "data" / "models_full",
        "label": "Full Features (Clinical + Tissue + Regional)",
        "drop_cols": [],
    }
}

app = FastAPI(title="Alzheimer Detection API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class _ArtifactCache:
    patients: list = []
    scaler: dict = {}
    model_globals: dict = {}  # Executed model globals
    feature_importance_cache: dict = {}
    scaler_p1: dict = {}

_cache = _ArtifactCache()

@app.on_event("startup")
def startup():
    logger.info("Loading OASIS-1 patient data JSON …")
    if DATA_JSON.exists():
        with open(DATA_JSON, "r") as f:
            _cache.patients = json.load(f)
        logger.info(f"  → {len(_cache.patients)} sessions loaded.")
    else:
        logger.warning(f"Patient data JSON not found at {DATA_JSON}")

    # Load full mode scaler (Phase 2)
    scaler_path = MODES["full"]["data_dir"] / "scaler.json"
    if scaler_path.exists():
        with open(scaler_path, "r") as f:
            _cache.scaler = json.load(f)
    
    # Load model code (Phase 2)
    for mode_key, mode_cfg in MODES.items():
        model_path = mode_cfg["models_dir"] / "model_p2_code.py"
        if model_path.exists():
            model_globals = {}
            with open(model_path, "r") as f:
                exec(f.read(), model_globals)
            _cache.model_globals[mode_key] = model_globals
            logger.info(f"  → Loaded Pure Python XGBoost [{mode_key}] from {model_path}")
            
        fi_path = mode_cfg["models_dir"] / "feature_importance.json"
        if fi_path.exists():
            with open(fi_path, "r") as f:
                _cache.feature_importance_cache[mode_key] = json.load(f)

    # Load Phase 1 Model
    phase1_model_path = API_ROOT / "data" / "phase1" / "model_p1_code.py"
    if phase1_model_path.exists():
        model_globals_p1 = {}
        with open(phase1_model_path, "r") as f:
            exec(f.read(), model_globals_p1)
        _cache.model_globals["phase1"] = model_globals_p1
        logger.info(f"  → Loaded Pure Python Phase 1 XGBoost from {phase1_model_path}")

    phase1_fi_path = API_ROOT / "data" / "phase1" / "feature_importance.json"
    if phase1_fi_path.exists():
        with open(phase1_fi_path, "r") as f:
            _cache.feature_importance_cache["phase1"] = json.load(f)

    phase1_scaler_path = API_ROOT / "data" / "processed" / "scaler.json"
    if phase1_scaler_path.exists():
        with open(phase1_scaler_path, "r") as f:
            _cache.scaler_p1 = json.load(f)

    logger.info("Startup complete.")

def _preprocess_row(row_dict: dict, mode_key: str) -> tuple:
    """Manual preprocessing using pure Python lists"""
    row = dict(row_dict)
    
    # Encode M/F
    mf = row.get("M/F")
    if mf in ["F", "f"]: row["M/F"] = 0.0
    elif mf in ["M", "m"]: row["M/F"] = 1.0
    else: row["M/F"] = 0.0
    
    # 1. Build full feature vector
    scaler_cols = _cache.scaler.get("feature_names_in_", [])
    if not scaler_cols:
        raise Exception("Missing feature names in scaler.json")
        
    X_full = [0.0] * len(scaler_cols)
    for i, col in enumerate(scaler_cols):
        val = row.get(col)
        if val is not None:
            try:
                X_full[i] = float(val)
            except:
                X_full[i] = 0.0

    # 2. Scale full vector
    mean_ = _cache.scaler["mean_"]
    scale_ = _cache.scaler["scale_"]
    
    X_scaled_full = []
    for val, m, s in zip(X_full, mean_, scale_):
        s_val = s if s != 0 else 1.0
        X_scaled_full.append((val - m) / s_val)
    
    # 3. Drop columns for ablation (if any)
    drop_cols = set(MODES[mode_key]["drop_cols"])
    
    # 4. Re-align (for full mode, it's just the same)
    # The generated Python score function expects inputs in the EXACT order of feature_names_in_
    features_after_drop = []
    X_final = []
    
    for feat in scaler_cols:
        if feat in drop_cols:
            continue
        try:
            idx = scaler_cols.index(feat)
            X_final.append(X_scaled_full[idx])
            features_after_drop.append(feat)
        except ValueError:
            pass
            
    return X_final, features_after_drop

@app.get("/api")
@app.get("/api/")
def read_root():
    return {"message": "NeuroScan AI Backend is running. Please access the web interface."}

@app.get("/api/patient-info")
def patient_info(session_id: str = DEFAULT_SESSION):
    row = next((r for r in _cache.patients if r.get("ID") == session_id), None)
    if not row:
        raise HTTPException(status_code=404, detail=f"Session '{session_id}' not found in JSON")

    clinical = {
        "session_id": session_id,
        "age": _safe_val(row, "Age"),
        "sex": _safe_val(row, "M/F"),
        "education": _safe_val(row, "Educ"),
        "ses": _safe_val(row, "SES"),
        "mmse": _safe_val(row, "MMSE"),
        "etiv": _safe_val(row, "eTIV"),
        "nwbv": _safe_val(row, "nWBV"),
        "asf": _safe_val(row, "ASF"),
        "cdr": _safe_val(row, "CDR"),
        "ground_truth": 1 if (row.get("CDR") is not None and float(row["CDR"]) > 0) else 0,
        "ground_truth_label": "Demented" if (row.get("CDR") is not None and float(row["CDR"]) > 0) else "Non-Demented",
    }
    return clinical

@app.get("/api/modes")
def get_modes():
    return [{"key": k, "label": v["label"]} for k, v in MODES.items()]

@app.post("/api/predict/{mode_key}")
def predict(mode_key: str, response: Response, session_id: str = DEFAULT_SESSION):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    
    if mode_key not in MODES:
        raise HTTPException(status_code=400, detail=f"Unknown mode '{mode_key}'")
    if mode_key not in _cache.model_globals:
        raise HTTPException(status_code=503, detail=f"Model for mode '{mode_key}' not loaded.")

    raw_row = next((r for r in _cache.patients if r.get("ID") == session_id), None)
    if not raw_row:
        raise HTTPException(status_code=404, detail=f"Session '{session_id}' not found")

    X_final, feature_names_used = _preprocess_row(raw_row, mode_key)
    model_globals = _cache.model_globals[mode_key]

    try:
        # Evaluate model using compiled python code
        # m2cgen generated score returns [prob_non_demented, prob_demented]
        prob_non_demented, prob_demented = model_globals["score"](X_final)
        pred = 1 if prob_demented >= 0.5 else 0
        confidence = prob_demented if pred == 1 else prob_non_demented
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {e}")

    raw_vals = {}
    for feat in feature_names_used:
        val = raw_row.get(feat)
        if val is None:
            raw_vals[feat] = None
        elif isinstance(val, str):
            raw_vals[feat] = val
        else:
            try:
                raw_vals[feat] = round(float(val), 4)
            except:
                raw_vals[feat] = str(val)

    fi = _cache.feature_importance_cache.get(mode_key, [])

    # Phase 1 Model
    phase1_results = {}
    if "phase1" in _cache.model_globals and _cache.scaler_p1:
        model_globals_p1 = _cache.model_globals["phase1"]
        mean_p1 = _cache.scaler_p1["mean_"]
        scale_p1 = _cache.scaler_p1["scale_"]
        
        scaler_cols_p1 = ['Age', 'Educ', 'SES', 'MMSE', 'eTIV', 'nWBV', 'ASF', 'Delay']
        X_scale = [0.0] * len(scaler_cols_p1)
        for i, c in enumerate(scaler_cols_p1):
            v = raw_row.get(c)
            X_scale[i] = float(v) if v is not None else 0.0
            
        X_scaled_dict = {}
        for c, val, m, s in zip(scaler_cols_p1, X_scale, mean_p1, scale_p1):
            s_val = s if s != 0 else 1.0
            X_scaled_dict[c] = (val - m) / s_val
        
        p1_feats = ['M/F', 'Age', 'Educ', 'SES', 'MMSE', 'eTIV', 'nWBV', 'ASF']
        X_p1 = [0.0] * len(p1_feats)
        for i, c in enumerate(p1_feats):
            if c == 'M/F':
                v = raw_row.get(c)
                if str(v).upper() in ['M', '1', '1.0']: X_p1[i] = 1.0
                else: X_p1[i] = 0.0
            else:
                X_p1[i] = X_scaled_dict[c]
                
        try:
            prob_non_demented_p1, prob_demented_p1 = model_globals_p1["score"](X_p1)
            pred_p1 = 1 if prob_demented_p1 >= 0.5 else 0
            
            fi_p1 = _cache.feature_importance_cache.get("phase1", [])
            phase1_results = {
                "prediction": pred_p1,
                "prediction_label": "Demented" if pred_p1 == 1 else "Non-Demented",
                "prob_demented": prob_demented_p1,
                "prob_non_demented": prob_non_demented_p1,
                "feature_importance": fi_p1[:5]
            }
        except Exception as e:
            logger.error(f"Phase 1 prediction failed: {e}")

    return {
        "session_id": session_id,
        "mode": mode_key,
        "mode_label": MODES[mode_key]["label"],
        "prediction": pred,
        "prediction_label": "Demented" if pred == 1 else "Non-Demented",
        "confidence": confidence,
        "prob_demented": prob_demented,
        "prob_non_demented": prob_non_demented,
        "num_features_used": len(feature_names_used),
        "features": raw_vals,
        "feature_importance": fi[:15],
        "phase1_results": phase1_results,
    }

def _safe_val(row, col):
    val = row.get(col)
    if val is None:
        return None
    if isinstance(val, float) and val.is_integer():
        return int(val)
    if isinstance(val, float):
        return round(val, 4)
    return val

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("index:app", host="0.0.0.0", port=8000, reload=True)
