import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# LOAD CLEANED DATA
# =========================
df = pd.read_csv("data/processed/cleaned_orders.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Set seaborn style
sns.set_style("whitegrid")

# =========================
# SALES TREND OVER TIME
# =========================
plt.figure(figsize=(14,6))

plt.plot(df["date"], df["sales"])

plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("reports/figures/sales_trend.png")

plt.show()

# =========================
# PRICE VS SALES
# =========================
plt.figure(figsize=(8,5))

sns.scatterplot(x=df["price"], y=df["sales"])

plt.title("Price vs Sales")

plt.tight_layout()

plt.savefig("reports/figures/price_vs_sales.png")

plt.show()

# =========================
# STOCK VS SALES
# =========================
plt.figure(figsize=(8,5))

sns.scatterplot(x=df["stock"], y=df["sales"])

plt.title("Stock vs Sales")

plt.tight_layout()

plt.savefig("reports/figures/stock_vs_sales.png")

plt.show()

# =========================
# CORRELATION HEATMAP
# =========================
plt.figure(figsize=(6,4))

correlation = df[["sales", "stock", "price"]].corr()

sns.heatmap(correlation, annot=True, cmap="Blues")

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("reports/figures/correlation_heatmap.png")

plt.show()

print("\nEDA COMPLETED SUCCESSFULLY!")