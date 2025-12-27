import requests
import datetime
import time
import sqlite3

conn = sqlite3.connect("crypto_project.db")
cursor = conn.cursor()

sql = """
CREATE TABLE IF NOT EXISTS crypto_logs(
id INTEGER PRIMARY KEY AUTOINCREMENT,
timestamp TEXT,
btc_price REAL,
eth_price REAL)
"""
cursor.execute(sql)
conn.commit()
conn.close()

print("--- CRYPTO BOT STARTED ---")
while True:
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=inr"
    try:
        response = requests.get(url)
        data = response.json()
        btc_val = data["bitcoin"]["inr"]
        eth_val = data["ethereum"]["inr"]
        now = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")

        conn = sqlite3.connect("crypto_project.db")
        cursor = conn.cursor()

        sql = "INSERT INTO crypto_logs (timestamp,btc_price,eth_price) VALUES(?,?,?)"
        cursor.execute(sql,(now,btc_val,eth_val))
        conn.commit()
        conn.close()

        print(f"{now} BTC: {btc_val} and ETH: {eth_val}")

    except Exception as e:
        print(f"error: {e}")
    
    time.sleep(10)
