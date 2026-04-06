import pandas as pd

def add_nutrition_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates new meaningful features for the ML model.
    """
    # 1. Protein-to-Calorie Ratio 
    # High protein with low calories is the 'Gold Standard' for fat loss
    df['protein_efficiency'] = df['protein_intake_g'] / (df['calorie_deficit'] + 1)
    
    # 2. Success Categorization (Target Engineering)
    # 0.5kg/week is 'Good', 1kg/week is 'Excellent'
    df['success_tier'] = pd.cut(df['weight_loss_kg'], 
                                bins=[-float('inf'), 0.4, 0.8, float('inf')], 
                                labels=['Maintenance', 'Steady', 'Optimal'])
    
    return df

import pandas as pd

def add_relative_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates relative nutritional metrics to improve model sensitivity.
    """
    # 1. Protein per KG (The Target Feature)
    df['protein_per_kg'] = df['protein_intake_g'] / df['current_weight_kg']
    
    # 2. Deficit Intensity 
    # A 500 calorie deficit is harder on a 70kg person than a 120kg person.
    df['deficit_intensity'] = df['calorie_deficit'] / df['current_weight_kg']
    
    # 3. Protein Efficiency Ratio (SDE Logic: Handling division by zero)
    df['protein_to_deficit_ratio'] = df['protein_intake_g'] / (df['calorie_deficit'] + 1)
    
    return df