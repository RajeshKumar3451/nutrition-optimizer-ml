import os
import pandas as pd
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class NutritionMetrics(BaseModel):
    protein_intake_g: float
    calorie_deficit: float
    current_weight_kg: float
    protein_per_kg: float

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if "src" in BASE_DIR:
    PROJECT_ROOT = os.path.dirname(BASE_DIR)
else:
    PROJECT_ROOT = BASE_DIR

MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "nutrition_rf_model.pkl")

model = None
if os.path.exists(MODEL_PATH):
    try:
        model = joblib.load(MODEL_PATH)
        print("✅ ML Brain Loaded!")
    except Exception as e:
        print(f"❌ Error loading model: {e}")
else:
    print(f"❌ Model not found at: {MODEL_PATH}")


@app.get("/")
async def serve_ui():
    index_path = os.path.join(PROJECT_ROOT, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"error": "index.html not found in root"}

@app.get("/status")
def get_status():
    return {"status": "online", "model_loaded": model is not None}

@app.post("/predict")
def predict_weight_loss(data: NutritionMetrics):
    if model is None:
        raise HTTPException(status_code=500, detail="Model missing on server.")
    
    input_df = pd.DataFrame([data.dict()])
    try:
        prediction = model.predict(input_df)[0]
        return {"predicted_weekly_loss_kg": round(prediction, 2)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))