import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# LOAD DATASET
# =========================
df = pd.read_csv("data/raw/orders.csv")

print("FIRST 5 ROWS")
print(df.head())

# =========================
# RENAME COLUMNS
# =========================
df.columns = ["date", "sales", "stock", "price"]

print("\nRENAMED COLUMNS")
print(df.columns)

# =========================
# CONVERT DATE COLUMN
# =========================
df["date"] = pd.to_datetime(df["date"])

# =========================
# SORT DATA
# =========================
df = df.sort_values("date")

# =========================
# CHECK DUPLICATES
# =========================
print("\nDUPLICATES:")
print(df.duplicated().sum())

# =========================
# DATA TYPES
# =========================
print("\nDATA TYPES")
print(df.dtypes)

# =========================
# BASIC STATISTICS
# =========================
print("\nSTATISTICS")
print(df.describe())

# =========================
# SAVE CLEANED DATA
# =========================
df.to_csv("data/processed/cleaned_orders.csv", index=False)

print("\nCleaned dataset saved successfully!")