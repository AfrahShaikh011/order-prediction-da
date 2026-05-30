import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from xgboost import XGBRegressor

# =========================
# LOAD DATA
# =========================
df = pd.read_csv(
    "data/processed/featured_orders.csv"
)

# =========================
# FEATURES & TARGET
# =========================
X = df.drop(columns=["date", "sales"])

y = df["sales"]

# =========================
# TRAIN TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# TRAIN MODEL
# =========================
model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=6,
    random_state=42
)

model.fit(X_train, y_train)

# =========================
# PREDICTIONS
# =========================
predictions = model.predict(X_test)

# =========================
# VISUALIZATION
# =========================
plt.figure(figsize=(14,6))

plt.plot(
    y_test.values[:100],
    label="Actual Sales"
)

plt.plot(
    predictions[:100],
    label="Predicted Sales"
)

plt.title("Actual vs Predicted Sales")

plt.xlabel("Samples")

plt.ylabel("Sales")

plt.legend()

plt.tight_layout()

plt.savefig(
    "reports/figures/prediction_comparison.png"
)

plt.show()

print("\nPrediction visualization completed!")