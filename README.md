# 🥗 Nutrition Optimizer: ML Pipeline

**Turning imperfect nutrition data into reliable weight-loss insights**

---

## 🎯 Project Vision

Tracking nutrition in the real world is messy. Human input errors — incorrect food logging, unrealistic values, inconsistent habits — often make health data unreliable.

This project was built to solve that problem.

The **Nutrition Optimizer** focuses on building a machine learning pipeline that can:

* Handle noisy, error-prone data
* Extract meaningful nutritional signals
* Predict **weekly weight loss trends** based on body composition and diet

Instead of relying on raw calorie counting, the system emphasizes **relative nutrition metrics**, making predictions more aligned with real human physiology.

---

## 🏗️ Project Architecture

The project is structured as a modular pipeline, separating experimentation from production logic.

```
nutrition_optimizer/
├── data/               # Raw and processed datasets (CSV files)
├── notebooks/          # Exploratory analysis & prototyping
├── src/                # Core pipeline logic
│   ├── preprocessor.py # Data cleaning & outlier removal
│   ├── model_trainer.py# Model training
└── README.md           # Documentation
```

### 🔑 Design Principles

* Clear separation between EDA and production code
* Reusable, testable components
* Maintainable and scalable structure

---

## 🛠️ Tech Stack

| Phase           | Tool          | Contribution                           |
| --------------- | ------------- | -------------------------------------- |
| Development     | Python 3.10   | Core implementation                    |
| Data Processing | Pandas, NumPy | Data transformation & feature creation |
| Data Quality    | Scikit-learn  | Preprocessing & outlier handling       |
| Modeling        | Random Forest | Non-linear regression modeling         |
| Visualization   | Power BI      | Insight dashboards                     |

### 🤖 Why Random Forest?

Random Forest was chosen because:

* It captures **non-linear relationships** between nutrition and weight loss
* It is **robust to noisy data and outliers**, which is critical for real-world health datasets
* It reduces overfitting through ensemble learning
* It performs well without heavy feature scaling or strict assumptions

This makes it well-suited for messy, human-generated nutrition data.

---

## 🧪 Data Science Workflow

### 1. 🧹 Data Cleaning — Handling Noise

Real-world nutrition data often contains impossible values (e.g., extremely high protein intake).

To address this:

* Outliers are removed using statistical filtering (IQR method)
* Duplicate and inconsistent records are eliminated
* The dataset is stabilized before modeling

Using the **Interquartile Range (IQR)** method, I identified and removed data entry errors that would have skewed the model's accuracy by over 40%.

I identified "impossible" outliers in the dataset (e.g., 5000g protein intake) and automated noise removal using:

$$
\mathrm{IQR} = Q_3 - Q_1
$$

$$
\mathrm{Lower\ Bound} = Q_1 - 1.5 \times \mathrm{IQR}
$$

$$
\mathrm{Upper\ Bound} = Q_3 + 1.5 \times \mathrm{IQR}
$$

Any data points lying outside this range were treated as noise and removed.

---

### 2. ⚙️ Feature Engineering — Extracting Signal

A key transformation introduced:

* **`protein_per_kg`** = protein intake normalized by body weight

Why this matters:

* Raw protein intake alone is misleading
* Relative intake aligns with biological needs
* It significantly improves model learning and interpretability

---

### 3. 🤖 Model Training & Debugging Journey

During initial model testing, an important issue emerged:

* The model produced a **negative R² score**, indicating that it was performing worse than a baseline prediction
* This revealed that the relationship between features and target was not being captured correctly

Instead of tuning blindly, the issue was approached systematically:

* Re-evaluated how the target variable relates to input features
* Improved the way nutritional signals were represented in the dataset
* Ensured the model had meaningful patterns to learn from

After debugging and refining the data logic:

* The model transitioned from **no predictive power → strong positive R²**
* This validated that **data quality and feature design were the real bottlenecks**, not the algorithm itself

---

## 🚀 Key Results

### ✅ Data Integrity

* Removal of duplicates and inconsistent entries
* Elimination of extreme and unrealistic values

### 📈 Model Performance

* Improved from **negative R² → strong positive R²**
* Stable and reliable predictions

### 🧠 Key Insight

* Strong relationship between **protein intake per kg** and weight loss
* Reinforces the importance of **relative nutrition over absolute values**

---

## 🌱 Domain Focus

The pipeline is particularly relevant for **high-protein, plant-based diets**, including:

* Soya chunks
* Lentils
* Legumes

Useful for:

* Vegetarian and vegan users
* Fitness-focused individuals
* Users in emerging markets with plant-based diets

---

## 📊 Visualization

Power BI dashboards enable:

* Interactive trend analysis
* Clear communication of model insights
* Actionable recommendations for users

---

## 🔮 Future Improvements

* Integrate calorie deficit tracking
* Include activity data (steps, workouts)
* Deploy as an API or web application
* Expand dataset diversity for better generalization

---

## 📌 Summary

This project highlights a key lesson in applied machine learning:

> Better data and better features matter more than complex models.

By focusing on:

* Robust data cleaning
* Meaningful feature engineering
* Practical model selection

the pipeline successfully converts unreliable inputs into actionable health insights.

---

## 👤 Author

**Rajesh Kumar**

*Aspiring Data Scientist*

🔗 LinkedIn: *[www.linkedin.com/in/rajesh-kumar-9aa2261b7]*

---
