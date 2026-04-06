from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def train_nutrition_model(df):
    # 1. Define Features (X) and Target (y)
    features = ['protein_intake_g', 'calorie_deficit', 'current_weight_kg', 'protein_per_kg']
    X = df[features]
    y = df['weight_loss_kg']
    
    # 2. Split into Training and Testing sets (80/20)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Initialize and Train
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 4. Evaluate
    predictions = model.predict(X_test)
    score = r2_score(y_test, predictions)
    
    print(f"Model trained! R-Squared Accuracy: {score:.4f}")
    return model