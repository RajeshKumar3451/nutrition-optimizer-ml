# 🥗 Nutrition Optimizer: End-to-End ML Pipeline
**Transforming "Dirty" Health Data into Actionable Weight Loss Predictions**

---

## 🎯 The Vision
In the world of health-tech, "Garbage In = Garbage Out." This project was born out of a personal and academic challenge: How do we build a predictive model that remains robust despite human data-entry errors? As a 187cm, 120kg individual pursuing a high-protein plant-based diet, I built this pipeline to move beyond simple calorie counting. 

## 🏗️ Project Architecture
Unlike standard notebook-only projects, this repository follows a **Modular Production Structure**. This ensures the code is reusable, testable, and scalable.

```text
nutrition_optimizer/
├── data/               # Multi-stage data versioning (Raw vs. Processed)
├── notebooks/          # Exploratory Data Analysis & Prototyping
├── src/                # Core Production Logic (The "Engine")
│   ├── __init__.py
│   ├── preprocessor.py # Automated cleaning & outlier detection
│   ├── feature_engineer.py # Domain-specific metric creation
│   └── model_trainer.py    # ML Model architecture (Random Forest)
├── requirements.txt    # Dependency Management
└── README.md           # Documentation

🛠️ Tool Integration & Workflow
I integrated multiple industry-standard tools to bridge the gap between raw data and business insights:

| Phase | Tool | Key Contribution |
| :--- | :--- | :--- |
| **Development** | Python (VS Code) | Built a modular `src` package for clean code separation. |
| **Data Quality** | Scikit-Learn | Implemented **IQR Statistical Filtering** to remove 40x outliers. |
| **Engineering** | Pandas / NumPy | Created the `protein_per_kg` feature to normalize results. |
| **Predictive AI** | Random Forest | Achieved a high R-Squared score by identifying non-linear patterns. |
| **Visualization** | Seaborn / Power BI | Translated complex ML metrics into clear, actionable dashboards. |

### 🧪 The "Data Science" Story

#### 1. The Cleaning Operation (IQR Method)
I identified "impossible" outliers in the raw dataset (e.g., 5000g protein intake). Using the **Interquartile Range**, I automated the removal of noise to ensure the model wasn't skewed by data-entry errors:

$$IQR = Q3 - Q1$$

#### 2. Feature Engineering: The "Signal"
By engineering **`protein_per_kg`**, I successfully increased the model's accuracy. This transformation proved that raw grams are a "noisy" predictor; the true signal lies in nutritional intake relative to the user's specific body mass.

## 🚀 Key Results

* **Data Integrity:** Achieved 100% removal of duplicates and "impossible" outliers, ensuring a clean baseline for model training.
* **Model Performance:** Successfully transitioned from a negative R-Squared (random noise) to a strong positive score, validating the engineered features.
* **Scalability:** Built a modular pipeline that can be re-run on new datasets with zero manual intervention.

---

**Developed by Rajesh Kumar** 
[Rajesh Kumar](www.linkedin.com/in/rajesh-kumar-9aa2261b7)