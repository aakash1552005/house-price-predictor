# 🏠 House Price Predictor

A machine learning web application that predicts California house prices 
using Random Forest Regression — trained on 20,640 real housing records.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31-red)
![Accuracy](https://img.shields.io/badge/R²%20Score-80.5%25-green)

## 🔗 Live Demo
👉 [Click here to try the app](YOUR_STREAMLIT_URL_HERE)

---

## 📌 Project Overview

This project predicts house prices in California based on features like 
median income, house age, location, and occupancy. Built end-to-end from 
raw data exploration to a deployed interactive web application.

| Model | R² Score | MAE | RMSE |
|---|---|---|---|
| Linear Regression | 57.6% | $53,320 | $74,558 |
| **Random Forest** | **80.5%** | **$32,754** | **$50,534** |

> Random Forest improved accuracy by **22.9%** over the baseline model.

---

## 📊 Dataset

- **Source:** California Housing Dataset (Sklearn built-in)
- **Size:** 20,640 houses × 9 features
- **Target:** House Price (in $100,000s)

| Feature | Description |
|---|---|
| MedInc | Median income of households in the area |
| HouseAge | Median age of houses in the area |
| AveRooms | Average number of rooms per household |
| AveBedrms | Average number of bedrooms per household |
| Population | Total population in the area |
| AveOccup | Average number of occupants per household |
| Latitude | Geographic latitude of the area |
| Longitude | Geographic longitude of the area |

---

## 🔍 Key Findings

- **MedInc** is the strongest predictor with **52% feature importance**
- **AveOccup** ranked 2nd at 14% — invisible in correlation analysis 
  but captured by Random Forest's non-linear learning
- **AveRooms & AveBedrms** showed 0.85 multicollinearity — 
  Random Forest correctly identified both as low importance (3-4%)
- Price distribution is **right-skewed** — majority of houses 
  priced between $100k–$200k
- Dataset has a **hard cap at $500,001** — a data artifact 
  visible in the price histogram

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.12 | Core programming language |
| Pandas | Data loading and manipulation |
| Numpy | Numerical computations |
| Matplotlib & Seaborn | Data visualization |
| Scikit-learn | ML models and evaluation |
| Joblib | Model serialization |
| Streamlit | Web application framework |

---

## 🏗️ Project Structure
```
house-price-predictor/
│
├── app.py                  # Streamlit web application
├── requirements.txt        # Python dependencies
├── rf_model.pkl            # Trained Random Forest model (138MB)
├── feature_names.pkl       # Feature names for prediction
├── notebook.ipynb          # Full EDA and model training notebook
└── README.md               # Project documentation
```

---

## 🚀 Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/house-price-predictor.git
cd house-price-predictor
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

**4. Open browser**
```
http://localhost:8501
```

---

## 📈 Model Performance
```
Training set  →  16,512 houses (80%)
Testing set   →   4,128 houses (20%)

Random Forest Results:
├── R² Score  :  0.8051  (80.5% accuracy)
├── MAE       :  $32,754 average error
└── RMSE      :  $50,534 worst case error
```

---

## 🔮 How It Works
```
User Input (8 features)
        ↓
Streamlit Web Interface
        ↓
Load Trained Random Forest Model (138MB)
        ↓
model.predict(input_data)
        ↓
Display Predicted House Price 💰
```

---

## 📉 Feature Importance
```
MedInc      ████████████████████████████  52%
AveOccup    ██████████                    14%
Latitude    ████████                       9%
Longitude   ███████                        8%
HouseAge    █████                          6%
AveRooms    ████                           4%
Population  ██                             3%
AveBedrms   ██                             3%
```

---

## 🎯 What I Learned

- End-to-end ML project workflow from EDA to deployment
- Importance of baseline models before complex ones
- How Random Forest captures non-linear patterns missed by Linear Regression
- Model explainability using Feature Importance
- Detecting and understanding multicollinearity in features
- Building and deploying production ML web applications

---

## 🔜 Future Improvements

- [ ] Add XGBoost model (target: 88% accuracy)
- [ ] Add SHAP values for individual prediction explanation
- [ ] Add neighborhood map visualization using Folium
- [ ] Add model confidence intervals
- [ ] Add data drift monitoring

---

## 👨‍💻 Author

**Aakash**
- 📧 your-email@gmail.com
- 💼 [LinkedIn](https://linkedin.com/in/YOUR_PROFILE)
- 🐙 [GitHub](https://github.com/YOUR_USERNAME)

---

## ⭐ If you found this useful, please star the repo!
```

---

## Before pushing — update 3 things:
```
1. YOUR_STREAMLIT_URL_HERE → add after deployment
2. YOUR_USERNAME → your GitHub username
3. your-email@gmail.com → your email
4. YOUR_PROFILE → your LinkedIn URL
```

---

## Your folder is now complete! ✅
```
📁 house_prediction
   ├── app.py               ✅
   ├── requirements.txt     ✅
   ├── README.md            ✅ just created!
   ├── rf_model.pkl         ✅
   └── feature_names.pkl    ✅
