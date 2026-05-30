import pandas as pd

# =========================
# LOAD CLEANED DATA
# =========================
df = pd.read_csv("data/processed/cleaned_orders.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# =========================
# DATE FEATURES
# =========================
df["day"] = df["date"].dt.day
df["month"] = df["date"].dt.month
df["year"] = df["date"].dt.year
df["day_of_week"] = df["date"].dt.dayofweek

# Weekend feature
df["is_weekend"] = df["day_of_week"].isin([5, 6]).astype(int)

# =========================
# LAG FEATURES
# =========================
df["lag_1"] = df["sales"].shift(1)
df["lag_7"] = df["sales"].shift(7)

# =========================
# ROLLING AVERAGES
# =========================
df["rolling_mean_7"] = df["sales"].rolling(window=7).mean()

df["rolling_mean_30"] = df["sales"].rolling(window=30).mean()

# =========================
# REMOVE NULLS
# =========================
df = df.dropna()

# =========================
# SAVE FEATURED DATASET
# =========================
df.to_csv(
    "data/processed/featured_orders.csv",
    index=False
)

# =========================
# DISPLAY RESULTS
# =========================
print("\nFEATURE ENGINEERING COMPLETED!\n")

print(df.head())

print("\nNEW COLUMNS:")
print(df.columns)