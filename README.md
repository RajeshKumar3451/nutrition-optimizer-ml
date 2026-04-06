# 🥗 Nutrition Optimizer: ML Pipeline

**Transforming imperfect nutrition data into reliable weight-loss insights**

---

## 🎯 Project Vision

This project addresses a common real-world problem: **human error in health and nutrition tracking**.

Food logs are often inconsistent — inaccurate portion sizes, incorrect entries, or missing values — which leads to unreliable conclusions. The **Nutrition Optimizer** is designed to work *despite* these imperfections.

It focuses on understanding how **body composition** and **nutritional intake** interact, enabling more accurate prediction of **weekly weight loss trends** and delivering practical dietary insights.

---

## 🏗️ Project Architecture

The project is structured as a **modular pipeline**, separating experimentation from production logic to ensure clarity and scalability.

```
nutrition_optimizer/
├── data/               # Raw and processed datasets (CSV files)
├── notebooks/          # Exploratory Data Analysis & prototyping
├── src/                # Core production logic
│   ├── preprocessor.py # Data cleaning (IQR-based outlier removal)
│   ├── model_trainer.py# Model training (Random Forest)
└── README.md           # Project documentation
```

### 🔑 Design Principles

* Clear separation between experimentation and core logic
* Reusable and maintainable components
* Structured pipeline for real-world applicability

---

## 🛠️ Tech Stack & Tooling

| Phase            | Tool         | Contribution                           |
| ---------------- | ------------ | -------------------------------------- |
| Development      | Python 3.10  | End-to-end pipeline implementation     |
| Data Quality     | Scikit-learn | Outlier handling and preprocessing     |
| Data Engineering | Pandas       | Feature engineering (`protein_per_kg`) |
| Visualization    | Power BI     | Interactive dashboards and insights    |

---

## 🧪 Data Science Workflow

### 1. 🧹 Data Cleaning — IQR Method

Real-world nutrition data often includes extreme outliers (e.g., unrealistic protein intake values).

The pipeline applies the **Interquartile Range (IQR)** method to:

* Remove statistically extreme values
* Preserve meaningful data distribution
* Improve downstream model reliability

---

### 2. ⚙️ Feature Engineering — Extracting Signal

A key feature introduced:

* **`protein_per_kg`** = protein intake normalized by body weight

This transformation:

* Adds biological relevance to raw data
* Improves signal quality
* Enables better learning of meaningful patterns

---

### 3. 🤖 Model Training

* Model: **Random Forest Regressor**
* Goal: Predict **weekly weight loss**

The model is designed to capture **non-linear relationships** between diet and weight change.

---

## 📊 The Debugging Journey (From Noise to Signal)

During initial testing, the model produced a **negative R² score**, indicating that it was performing worse than a baseline — a clear sign that the model wasn’t learning any meaningful relationship from the data.

Instead of tuning the model blindly, the focus shifted to the **data itself**:

* Re-evaluated how the target variable (weight loss) was represented
* Identified weak relationships between input features and output
* Refined the data generation and feature relationships to better reflect realistic physiological patterns

After these corrections, the model began to capture meaningful trends, resulting in a **strong positive R² score**.

This process reinforced a key insight:

> **Model performance is driven more by data quality and feature relevance than by algorithm complexity.**

---

## 🚀 Key Results

### ✅ Data Integrity

* Complete removal of duplicates
* Elimination of unrealistic and extreme outliers

### 📈 Model Performance

* Improved from **negative R² (no predictive signal)**
* To **strong positive R² (reliable predictions)**

### 🧠 Domain Insight

* Strong relationship between **protein intake per kg** and weight loss
* Supports structured, high-protein dietary strategies

---

## 🌱 Domain Focus

The pipeline is particularly relevant for **high-protein, plant-based diets**, including foods such as:

* Soya chunks
* Lentils
* Legumes

Applicable for:

* Vegetarian and vegan users
* Fitness-focused individuals
* Data-driven nutrition tracking

---

## 📊 Visualization

Power BI dashboards provide:

* Clear trend analysis
* Interactive exploration
* Accessible insights for non-technical users

---

## 🔮 Future Improvements

* Incorporate calorie deficit tracking
* Integrate wearable data (activity, steps, sleep)
* Deploy as an API or web application
* Expand dataset diversity for broader generalization

---

## 📌 Summary

This project demonstrates how combining **clean data pipelines**, **thoughtful feature engineering**, and **iterative debugging** can turn unreliable inputs into meaningful predictions.

It highlights an important principle in applied machine learning:

> **Better data beats more complex models.**

---

## 👤 Author

**Rajesh Kumar**

🔗 LinkedIn: *[www.linkedin.com/in/rajesh-kumar-9aa2261b7]*

---
