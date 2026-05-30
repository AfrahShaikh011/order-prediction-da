from flask import Flask, jsonify, send_file
from flask_cors import CORS

import pandas as pd
import joblib
import os

app = Flask(__name__)

CORS(app)

# =========================
# DEPLOYMENT SAFE PATHS
# =========================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "best_model.pkl"
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "processed",
    "featured_orders.csv"
)

# =========================
# LOAD MODEL & DATA
# =========================

model = joblib.load(MODEL_PATH)

df = pd.read_csv(DATA_PATH)

# =========================
# PREDICT ROUTE
# =========================

@app.route("/predict", methods=["GET"])
def predict():

    # Latest record

    latest_data = df.iloc[-1:]

    X_future = latest_data.drop(
        columns=["date", "sales"]
    )

    prediction = float(
        model.predict(X_future)[0]
    )

    # =========================
    # ACTUAL VS PREDICTED
    # =========================

    comparison_df = df.tail(30).copy()

    X_compare = comparison_df.drop(
        columns=["date", "sales"]
    )

    comparison_df["predicted_sales"] = model.predict(
        X_compare
    ).astype(float)

    chart_data = comparison_df[
        ["date", "sales", "predicted_sales"]
    ].to_dict(orient="records")

    # =========================
    # FUTURE FORECAST
    # =========================

    future_forecast = []

    latest_row = df.iloc[-1:].copy()

    future_date = pd.to_datetime(
        latest_row["date"].values[0]
    )

    for _ in range(7):

        X_future = latest_row.drop(
            columns=["date", "sales"]
        )

        future_sales = float(
            model.predict(X_future)[0]
        )

        future_date += pd.Timedelta(days=1)

        future_forecast.append({

            "date": future_date.strftime(
                "%Y-%m-%d"
            ),

            "forecast": round(
                future_sales,
                2
            )
        })

    return jsonify({

        "predicted_sales": round(
            prediction,
            2
        ),

        "model": "XGBoost",

        "mae": 30.21,

        "rmse": 43.20,

        "r2_score": 0.6610,

        "chart_data": chart_data,

        "future_forecast": future_forecast
    })


# =========================
# DOWNLOAD FORECAST CSV
# =========================

@app.route("/download-forecast", methods=["GET"])
def download_forecast():

    latest_row = df.iloc[-1:].copy()

    future_forecast = []

    future_date = pd.to_datetime(
        latest_row["date"].values[0]
    )

    for _ in range(7):

        X_future = latest_row.drop(
            columns=["date", "sales"]
        )

        future_sales = float(
            model.predict(X_future)[0]
        )

        future_date += pd.Timedelta(days=1)

        future_forecast.append({

            "date": future_date.strftime(
                "%Y-%m-%d"
            ),

            "forecast": round(
                future_sales,
                2
            )
        })

    forecast_df = pd.DataFrame(
        future_forecast
    )

    csv_path = os.path.join(
        BASE_DIR,
        "forecast.csv"
    )

    forecast_df.to_csv(
        csv_path,
        index=False
    )

    return send_file(
        csv_path,
        as_attachment=True
    )


# =========================
# HEALTH CHECK
# =========================

@app.route("/")
def home():

    return jsonify({

        "status": "running",

        "message": "Order Prediction API is live"
    })


# =========================
# START APP
# =========================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )