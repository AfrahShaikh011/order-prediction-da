import pandas as pd
import joblib

# =========================
# LOAD DATA
# =========================
df = pd.read_csv(
    "data/processed/featured_orders.csv"
)

# =========================
# LOAD SAVED MODEL
# =========================
model = joblib.load(
    "models/best_model.pkl"
)

# =========================
# GET LATEST RECORD
# =========================
latest_data = df.iloc[-1:]

# =========================
# PREPARE FEATURES
# =========================
X_future = latest_data.drop(
    columns=["date", "sales"]
)

# =========================
# PREDICT FUTURE SALES
# =========================
future_prediction = model.predict(X_future)

# =========================
# DISPLAY RESULT
# =========================
print("\n=========================")
print("FUTURE SALES PREDICTION")
print("=========================")

print(
    f"Predicted Next Day Sales: "
    f"{future_prediction[0]:.2f}"
)