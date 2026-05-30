import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.ensemble import RandomForestRegressor

from xgboost import XGBRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import joblib

# =========================
# LOAD FEATURED DATA
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
# MODELS
# =========================
models = {
    "Linear Regression": LinearRegression(),
    
    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ),

    "XGBoost": XGBRegressor(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=6,
        random_state=42
    )
}

# =========================
# TRAIN & EVALUATE
# =========================
best_model = None
best_r2 = -999

for name, model in models.items():

    print(f"\nTRAINING: {name}")

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    rmse = np.sqrt(
        mean_squared_error(
            y_test,
            predictions
        )
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R2 SCORE: {r2:.4f}")

    # Save best model
    if r2 > best_r2:
        best_r2 = r2
        best_model = model

# =========================
# SAVE BEST MODEL
# =========================
joblib.dump(
    best_model,
    "models/best_model.pkl"
)

print("\nBEST MODEL SAVED SUCCESSFULLY!")