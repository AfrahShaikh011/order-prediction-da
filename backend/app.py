from flask import Flask, jsonify, send_file
from flask_cors import CORS

import pandas as pd
import joblib

app = Flask(__name__)

CORS(app)

# =========================
# LOAD MODEL
# =========================

model = joblib.load(
    "../models/best_model.pkl"
)

# =========================
# LOAD DATA
# =========================

df = pd.read_csv(
    "../data/processed/featured_orders.csv"
)

# =========================
# PREDICT ROUTE
# =========================

@app.route("/predict", methods=["GET"])
def predict():

    # =========================
    # LATEST DATA
    # =========================

    latest_data = df.iloc[-1:]

    X_future = latest_data.drop(
        columns=["date", "sales"]
    )

    prediction = model.predict(
        X_future
    )[0]

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

    for i in range(7):

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
                future_sales, 2
            )
        })

    # =========================
    # RETURN RESPONSE
    # =========================

    return jsonify({

        "predicted_sales": round(
            float(prediction), 2
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

    for i in range(7):

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
                future_sales, 2
            )
        })

    forecast_df = pd.DataFrame(
        future_forecast
    )

    file_path = "forecast.csv"

    forecast_df.to_csv(
        file_path,
        index=False
    )

    return send_file(
        file_path,
        as_attachment=True
    )

if __name__ == "__main__":

    app.run(debug=True)