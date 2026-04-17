import os
import pandas as pd
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Nutrition Optimizer - Core ML API")

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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "nutrition_rf_model.pkl")

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    print("✅ ML Brain Loaded: Random Forest Model Ready!")
else:
    model = None
    print(f"❌ ERROR: Model file not found at {MODEL_PATH}")


@app.get("/")
def read_root():
    return {"message": "Nutrition Optimizer API is Online", "model_status": "Loaded" if model else "Missing"}

@app.post("/predict")
def predict_weight_loss(data: NutritionMetrics):
    if model is None:
        raise HTTPException(status_code=500, detail="Machine Learning model is not loaded.")

    input_df = pd.DataFrame([data.dict()])
    
    try:
        prediction = model.predict(input_df)[0]
        return {
            "predicted_weekly_loss_kg": round(prediction, 2),
            "status": "Success"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")
    
@app.get("/")
async def read_index():
    return FileResponse('index.html')