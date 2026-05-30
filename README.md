# 🚀 AI-Powered Order Forecasting Dashboard

A full-stack machine learning web application that predicts future product orders and visualizes business insights through an interactive dashboard.

## 🌐 Live Demo

**Frontend:** https://order-prediction-da.vercel.app/

**Backend API:** https://order-prediction-da.onrender.com/

---

## 📌 Project Overview

The AI-Powered Order Forecasting Dashboard helps businesses forecast future sales using historical order data and machine learning models.

The application processes historical sales records, engineers meaningful features, trains multiple machine learning models, selects the best-performing model, and serves predictions through a Flask API. A React-based dashboard visualizes forecasting results, model performance metrics, and business analytics.

---

## ✨ Features

### Machine Learning

* Data preprocessing and cleaning
* Feature engineering
* Multiple model comparison
* Linear Regression
* Random Forest Regressor
* XGBoost Regressor
* Best model selection and persistence
* Future sales forecasting

### Dashboard

* Interactive React dashboard
* Actual vs Predicted Sales visualization
* 7-Day Future Forecast chart
* Business analytics dashboard
* Prediction insights page
* Responsive UI
* Dark theme interface

### Backend

* Flask REST API
* Prediction endpoint
* Forecast generation endpoint
* CSV forecast export
* Model loading using Joblib
* Cross-Origin Resource Sharing (CORS)

### Deployment

* Frontend deployed on Vercel
* Backend deployed on Render
* Production-ready architecture

---

## 🛠️ Tech Stack

### Frontend

* React.js
* Vite
* Tailwind CSS
* Recharts
* React Router DOM
* Axios
* React Hot Toast

### Backend

* Flask
* Flask-CORS
* Pandas
* NumPy
* Joblib

### Machine Learning

* Scikit-Learn
* XGBoost
* Random Forest
* Linear Regression

### Deployment

* Vercel
* Render
* GitHub

---

## 📊 Machine Learning Workflow

### 1. Data Collection

Historical order and inventory dataset containing:

* Sales
* Inventory
* Price
* Date

### 2. Data Preprocessing

* Column renaming
* Data type conversion
* Missing value handling
* Duplicate removal

### 3. Feature Engineering

Created advanced features including:

* Day
* Month
* Year
* Day of Week
* Weekend Indicator
* Lag-1 Sales
* Lag-7 Sales
* Rolling Mean (7 Days)
* Rolling Mean (30 Days)

### 4. Model Training

Models evaluated:

| Model             | MAE   | RMSE  | R² Score |
| ----------------- | ----- | ----- | -------- |
| Linear Regression | 34.67 | 47.98 | 0.5818   |
| Random Forest     | 32.69 | 45.58 | 0.6227   |
| XGBoost           | 30.21 | 43.20 | 0.6610   |

### Best Performing Model

**XGBoost Regressor**

* MAE: 30.21
* RMSE: 43.20
* R² Score: 0.6610

---

## 📈 Dashboard Components

### Dashboard Page

* Predicted Sales KPI
* Model Information
* RMSE Metric
* R² Score Metric
* Actual vs Predicted Sales Chart
* 7-Day Future Forecast Chart
* Forecast CSV Download

### Analytics Page

* Revenue Analytics
* Sales Insights
* Interactive Visualizations

### Predictions Page

* Forecast Trends
* Model Performance Insights
* Future Prediction Analysis

---

## 📂 Project Structure

```text
order-prediction-dashboard/
│
├── backend/
│   ├── app.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   └── package.json
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   └── best_model.pkl
│
├── reports/
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   └── future_prediction.py
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/AfrahShaikh011/order-prediction-da.git
cd order-prediction-da
```

### Backend Setup

```bash
cd backend

pip install -r requirements.txt

python app.py
```

Backend runs on:

```text
http://localhost:5000
```

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

## 🔗 API Endpoints

### Home Route

```http
GET /
```

Returns API status.

### Prediction Route

```http
GET /predict
```

Returns:

* Predicted Sales
* Actual vs Predicted Data
* Future Forecast Data

### Forecast Download

```http
GET /download-forecast
```

Downloads forecast results as CSV.

---

## 🚀 Future Enhancements

* CSV Upload System
* Real-Time Forecasting
* Authentication & User Accounts
* Cloud Database Integration
* Advanced Time-Series Models
* Forecast Confidence Intervals
* Multi-Product Forecasting
* Interactive Report Generation

---

## 👨‍💻 Author

**Afrah Shaikh**

Computer Engineering Student (TE)

GitHub: https://github.com/AfrahShaikh011

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
