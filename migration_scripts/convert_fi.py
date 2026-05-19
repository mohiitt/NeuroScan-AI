import pandas as pd
import json
import os

os.makedirs("webapp_vercel/api/data/models_full", exist_ok=True)
os.makedirs("webapp_vercel/api/data/phase1", exist_ok=True)

# Phase 2
df_p2 = pd.read_csv("results/phase2/models_full/xgboost_feature_importance.csv")
records_p2 = df_p2.to_dict(orient="records")
with open("webapp_vercel/api/data/models_full/feature_importance.json", "w") as f:
    json.dump(records_p2, f)

# Phase 1
df_p1 = pd.read_csv("models/phase1_oasis1/xgboost_feature_importance.csv")
records_p1 = df_p1.to_dict(orient="records")
with open("webapp_vercel/api/data/phase1/feature_importance.json", "w") as f:
    json.dump(records_p1, f)

print("Feature importances converted to JSON!")
