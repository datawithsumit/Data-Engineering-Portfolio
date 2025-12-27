import pandas as pd
import sqlite3

conn = sqlite3.connect("crypto_project.db")

sql = "SELECT * FROM crypto_logs"
df = pd.read_sql(sql, conn)

print("--- DATA REPORT ---")
print(df)

print("\n--- STATISTICS REPORT ---")
avg_btc = df["btc_price"].mean()
max_eth = df["eth_price"].max()

print(f"Average bitcoin price: {round(avg_btc,2)}")
print(f"Max Ethereum price: {max_eth}")

df["ratio"] = df["btc_price"]/df["eth_price"]

print("---PRICE OF 1 ETH to BTC")
print(df[["timestamp","ratio"]].tail())

conn.close()
