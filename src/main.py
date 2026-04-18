import os
import pandas as pd
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

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

# --- BULLETPROOF PATHING ---
# 1. Get the path where main.py is (which is inside 'src')
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# 2. Go up one level to reach the Project Root
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

# 3. Define absolute paths to your assets
INDEX_PATH = os.path.join(PROJECT_ROOT, "frontend", "index.html")
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "nutrition_rf_model.pkl")

# --- LOAD MODEL ---
model = None
if os.path.exists(MODEL_PATH):
    try:
        model = joblib.load(MODEL_PATH)
        print(f"✅ Success: Model loaded from {MODEL_PATH}")
    except Exception as e:
        print(f"❌ Load Error: {e}")
else:
    print(f"❌ ERROR: Model file not found at {MODEL_PATH}")

# --- ROUTES ---

@app.get("/")
async def serve_ui():
    if os.path.exists(INDEX_PATH):
        return FileResponse(INDEX_PATH)
    return {
        "error": "index.html not found",
        "debug_path_tried": INDEX_PATH,
        "current_working_dir": os.getcwd()
    }

@app.get("/favicon.ico")
async def favicon():
    favicon_path = os.path.join(PROJECT_ROOT, "frontend", "favicon.ico")
    if os.path.exists(favicon_path):
        return FileResponse(favicon_path)
    return {"error": "favicon not found"}

@app.post("/predict")
def predict_weight_loss(data: NutritionMetrics):
    if model is None:
        raise HTTPException(status_code=500, detail="Model file is missing on the server.")
    
    input_df = pd.DataFrame([data.dict()])
    try:
        prediction = model.predict(input_df)[0]
        return {"predicted_weekly_loss_kg": round(prediction, 2)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))