import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")

df = pd.read_sql("SELECT * from orders", conn)
conn.close()

df["total_sales"] = df["price"] * df["quantity"]

print("---RAW DATA---")
print(df.head())

print("\n ----- STATISTICAL ANALYSIS -----")
total_revenue = df["total_sales"].sum()
print(f"\n💰 TOTAL REVENUE: ₹{total_revenue}")

best_city = df.groupby("city")["total_sales"].sum()
print(f"\n🏙️ SALES BY CITY: {best_city}")

best_category = df.groupby("category")["total_sales"].sum()
print(f"\n📦 ORDERS BY CATEGORY: {best_category}")
