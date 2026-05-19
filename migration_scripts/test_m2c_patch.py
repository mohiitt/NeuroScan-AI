import m2cgen as m2c
import joblib

model_p2 = joblib.load("results/phase2/models_full/xgboost_model.pkl")
model_p2.feature_weights = None
model_p2.base_score = 0.5

print("Generating python code for Phase 2 model with base_score monkeypatch...")
try:
    code = m2c.export_to_python(model_p2)
    print("Success! Code length:", len(code))
except Exception as e:
    import traceback
    traceback.print_exc()
