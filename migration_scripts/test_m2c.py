import m2cgen as m2c
import joblib

model_p2 = joblib.load("results/phase2/models_full/xgboost_model.pkl")
booster = model_p2.get_booster()

print("Generating python code from booster...")
try:
    code = m2c.export_to_python(booster)
    print("Success! Code length:", len(code))
except Exception as e:
    print("Failed:", e)
