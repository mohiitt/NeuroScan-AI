import m2cgen as m2c
import joblib
import os

# Load the scikit-learn XGBClassifier models
model_p2 = joblib.load("results/phase2/models_full/xgboost_model.pkl")
model_p2.feature_weights = None
model_p2.base_score = 0.5

model_p1 = joblib.load("models/phase1_oasis1/xgboost_model.pkl")
model_p1.feature_weights = None
model_p1.base_score = 0.5

print("Generating python code for Phase 2 model...")
code_p2 = m2c.export_to_python(model_p2)
with open("webapp_vercel/api/data/models_full/model_p2_code.py", "w") as f:
    f.write(code_p2)

print("Generating python code for Phase 1 model...")
code_p1 = m2c.export_to_python(model_p1)
with open("webapp_vercel/api/data/phase1/model_p1_code.py", "w") as f:
    f.write(code_p1)

print("Conversion to pure Python code complete!")
