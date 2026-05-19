"""
Alzheimer's Disease Detection - FastAPI Backend
Serves feature extraction and XGBoost inference for the Phase 2 pipeline.
(Lightweight Vercel version: Pandas and scikit-learn removed)
"""

import json
import logging
from pathlib import Path
import csv

import numpy as np
import xgboost as xgb
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
    model_cache: dict = {}
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
    
    # Load models
    for mode_key, mode_cfg in MODES.items():
        model_path = mode_cfg["models_dir"] / "xgboost_model.json"
        if model_path.exists():
            booster = xgb.Booster()
            booster.load_model(str(model_path))
            _cache.model_cache[mode_key] = booster
            logger.info(f"  → Loaded XGBoost [{mode_key}] from {model_path}")
            
        fi_path = mode_cfg["models_dir"] / "xgboost_feature_importance.csv"
        if fi_path.exists():
            fi_list = []
            with open(fi_path, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # convert numeric values
                    for k,v in row.items():
                        try:
                            row[k] = float(v)
                        except:
                            pass
                    fi_list.append(row)
            _cache.feature_importance_cache[mode_key] = fi_list

    # Load Phase 1 Model
    phase1_model_path = API_ROOT / "data" / "phase1" / "xgboost_model.json"
    if phase1_model_path.exists():
        booster_p1 = xgb.Booster()
        booster_p1.load_model(str(phase1_model_path))
        _cache.model_cache["phase1"] = booster_p1
        logger.info(f"  → Loaded Phase 1 XGBoost from {phase1_model_path}")

    phase1_fi_path = API_ROOT / "data" / "phase1" / "xgboost_feature_importance.csv"
    if phase1_fi_path.exists():
        fi_list = []
        with open(phase1_fi_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                for k,v in row.items():
                    try:
                        row[k] = float(v)
                    except:
                        pass
                fi_list.append(row)
        _cache.feature_importance_cache["phase1"] = fi_list

    phase1_scaler_path = API_ROOT / "data" / "processed" / "scaler.json"
    if phase1_scaler_path.exists():
        with open(phase1_scaler_path, "r") as f:
            _cache.scaler_p1 = json.load(f)

    logger.info("Startup complete.")

def _preprocess_row(row_dict: dict, mode_key: str) -> tuple:
    """Manual preprocessing without pandas/sklearn"""
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
        
    X_full = np.zeros(len(scaler_cols))
    for i, col in enumerate(scaler_cols):
        val = row.get(col)
        if val is not None:
            try:
                X_full[i] = float(val)
            except:
                X_full[i] = 0.0

    # 2. Scale full vector
    mean_ = np.array(_cache.scaler["mean_"])
    scale_ = np.array(_cache.scaler["scale_"])
    # prevent div by zero just in case
    scale_ = np.where(scale_ == 0, 1.0, scale_)
    X_scaled_full = (X_full - mean_) / scale_
    
    # 3. Drop columns for ablation (if any)
    drop_cols = set(MODES[mode_key]["drop_cols"])
    
    # 4. Re-align (for full mode, it's just the same)
    # The XGBoost booster expects DMatrix. We need feature names.
    booster = _cache.model_cache.get(mode_key)
    model_feature_names = booster.feature_names if booster else scaler_cols
    
    X_final = []
    features_after_drop = []
    
    for feat in model_feature_names:
        if feat in drop_cols:
            continue
        try:
            idx = scaler_cols.index(feat)
            X_final.append(X_scaled_full[idx])
            features_after_drop.append(feat)
        except ValueError:
            pass
            
    X = np.array([X_final])
    dmatrix = xgb.DMatrix(X, feature_names=features_after_drop)
    return dmatrix, features_after_drop

@app.get("/")
def read_root():
    return {"message": "NeuroScan AI Backend is running. Please access the web interface."}

@app.get("/patient-info")
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

@app.get("/modes")
def get_modes():
    return [{"key": k, "label": v["label"]} for k, v in MODES.items()]

@app.post("/predict/{mode_key}")
def predict(mode_key: str, response: Response, session_id: str = DEFAULT_SESSION):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    
    if mode_key not in MODES:
        raise HTTPException(status_code=400, detail=f"Unknown mode '{mode_key}'")
    if mode_key not in _cache.model_cache:
        raise HTTPException(status_code=503, detail=f"Model for mode '{mode_key}' not loaded.")

    raw_row = next((r for r in _cache.patients if r.get("ID") == session_id), None)
    if not raw_row:
        raise HTTPException(status_code=404, detail=f"Session '{session_id}' not found")

    dmatrix, feature_names_used = _preprocess_row(raw_row, mode_key)
    booster = _cache.model_cache[mode_key]

    try:
        # XGBoost Booster predict returns probabilities for binary classification by default
        proba_val = booster.predict(dmatrix)[0]
        prob_demented = float(proba_val)
        prob_non_demented = 1.0 - prob_demented
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
    if "phase1" in _cache.model_cache and _cache.scaler_p1:
        booster_p1 = _cache.model_cache["phase1"]
        mean_p1 = np.array(_cache.scaler_p1["mean_"])
        scale_p1 = np.array(_cache.scaler_p1["scale_"])
        scale_p1 = np.where(scale_p1 == 0, 1.0, scale_p1)
        
        scaler_cols_p1 = ['Age', 'Educ', 'SES', 'MMSE', 'eTIV', 'nWBV', 'ASF', 'Delay']
        X_scale = np.zeros(len(scaler_cols_p1))
        for i, c in enumerate(scaler_cols_p1):
            v = raw_row.get(c)
            X_scale[i] = float(v) if v is not None else 0.0
            
        X_scaled_arr = (X_scale - mean_p1) / scale_p1
        X_scaled_dict = {c: X_scaled_arr[i] for i,c in enumerate(scaler_cols_p1)}
        
        p1_feats = ['M/F', 'Age', 'Educ', 'SES', 'MMSE', 'eTIV', 'nWBV', 'ASF']
        X_p1 = np.zeros(len(p1_feats))
        for i, c in enumerate(p1_feats):
            if c == 'M/F':
                v = raw_row.get(c)
                if str(v).upper() in ['M', '1', '1.0']: X_p1[i] = 1.0
                else: X_p1[i] = 0.0
            else:
                X_p1[i] = X_scaled_dict[c]
                
        dmat_p1 = xgb.DMatrix(np.array([X_p1]), feature_names=p1_feats)
        try:
            prob_p1 = float(booster_p1.predict(dmat_p1)[0])
            pred_p1 = 1 if prob_p1 >= 0.5 else 0
            
            fi_p1 = _cache.feature_importance_cache.get("phase1", [])
            phase1_results = {
                "prediction": pred_p1,
                "prediction_label": "Demented" if pred_p1 == 1 else "Non-Demented",
                "prob_demented": prob_p1,
                "prob_non_demented": 1.0 - prob_p1,
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
