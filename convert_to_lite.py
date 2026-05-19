import joblib
import pandas as pd
import json
import numpy as np
import math

# Convert CSV to JSON
df = pd.read_csv("webapp_vercel/api/data/oasis1_full_enhanced_features.csv")
records = df.to_dict(orient="records")
# Fix NaNs to null for JSON
for r in records:
    for k, v in r.items():
        if isinstance(v, float) and math.isnan(v):
            r[k] = None
with open("webapp_vercel/api/data/patient_data.json", "w") as f:
    json.dump(records, f)

# Convert phase 2 scaler
scaler_p2 = joblib.load("webapp_vercel/api/data/data_full/scaler.pkl")
with open("webapp_vercel/api/data/data_full/scaler.json", "w") as f:
    json.dump({
        "mean_": scaler_p2.mean_.tolist(),
        "scale_": scaler_p2.scale_.tolist(),
        "feature_names_in_": scaler_p2.feature_names_in_.tolist() if hasattr(scaler_p2, "feature_names_in_") else None
    }, f)

# Convert phase 1 scaler
scaler_p1 = joblib.load("webapp_vercel/api/data/processed/scaler.pkl")
with open("webapp_vercel/api/data/processed/scaler.json", "w") as f:
    json.dump({
        "mean_": scaler_p1.mean_.tolist(),
        "scale_": scaler_p1.scale_.tolist()
    }, f)

# Convert models
model_p2 = joblib.load("webapp_vercel/api/data/models_full/xgboost_model.pkl")
model_p2.save_model("webapp_vercel/api/data/models_full/xgboost_model.json")

model_p1 = joblib.load("webapp_vercel/api/data/phase1/xgboost_model.pkl")
model_p1.save_model("webapp_vercel/api/data/phase1/xgboost_model.json")

print("Conversion complete!")
