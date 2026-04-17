import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os

def train_nutrition_model(df):
    # Features must match your CSV column names exactly!
    features = ['protein_intake_g', 'calorie_deficit', 'current_weight_kg', 'protein_per_kg']
    X = df[features]
    y = df['weight_loss_kg']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    print(f"✅ Model trained! R2 Score: {model.score(X_test, y_test):.4f}")
    return model

# --- EXECUTION LOGIC ---
# This looks for the data relative to THIS script's location
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, "data", "processed", "final_nutrition_data.csv")

import os
import pandas as pd


script_dir = os.path.dirname(os.path.abspath(__file__))

project_root = os.path.dirname(script_dir)

data_path = os.path.join(project_root, "data", "processed", "final_nutrition_data.csv")

print(f"🔍 Python is looking for data at: {data_path}")

if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    print("✅ Data loaded successfully!")
    
    rf_model = train_nutrition_model(df)
    model_dir = os.path.join(project_root, "models")
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(rf_model, os.path.join(model_dir, "nutrition_rf_model.pkl"))
    print("🚀 SUCCESS: Model saved in /models/ folder!")

else:
    print(f"❌ ERROR: Still can't find it. Is the file named exactly 'final_nutrition_data.csv'?")
    print(f"Inside your 'data/processed' folder, I see these files: {os.listdir(os.path.join(project_root, 'data', 'processed')) if os.path.exists(os.path.join(project_root, 'data', 'processed')) else 'Folder not found'}")