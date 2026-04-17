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

# --- SMART PATH SEARCHING ---
def find_path(target_name):
    # Search in current folder, then one level up, then in common subfolders
    possible_paths = [
        target_name,
        os.path.join("..", target_name),
        os.path.join("src", target_name),
        os.path.join("..", "src", target_name)
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return os.path.abspath(path)
    return None

# Find index.html and the models folder
INDEX_PATH = find_path("index.html")
MODEL_DIR = find_path("models")
MODEL_FILE = os.path.join(MODEL_DIR, "nutrition_rf_model.pkl") if MODEL_DIR else None

model = None
if MODEL_FILE and os.path.exists(MODEL_FILE):
    try:
        model = joblib.load(MODEL_FILE)
        print(f"✅ Model loaded from: {MODEL_FILE}")
    except Exception as e:
        print(f"❌ Load error: {e}")
else:
    print(f"❌ Model missing! Looked in: {MODEL_FILE}")

# --- ROUTES ---

@app.get("/")
async def serve_ui():
    if INDEX_PATH:
        return FileResponse(INDEX_PATH)
    return {"error": "index.html not found. Check if it was pushed to GitHub!"}

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
    
@app.get("/")
async def serve_ui():
    # This specifically looks into the 'frontend' folder
    paths_to_try = [
        "index.html", 
        "frontend/index.html", 
        "../frontend/index.html",
        "src/frontend/index.html"
    ]
    for path in paths_to_try:
        if os.path.exists(path):
            print(f"✅ Found UI at: {path}")
            return FileResponse(path)
    
    return {"error": f"index.html not found. Check GitHub for frontend/index.html"}