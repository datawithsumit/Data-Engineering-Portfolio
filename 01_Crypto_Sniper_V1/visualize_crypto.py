import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# --- Settings ---
DB_NAME = "crypto_project.db"
IMAGE_NAME = "crypto_price_trend.png"

def plot_trends():
    if not os.path.exists(DB_NAME):
        print(f"❌ Error: {DB_NAME} not found.")
        return

    try:
        conn = sqlite3.connect(DB_NAME)
        df = pd.read_sql("SELECT * FROM crypto_logs", conn)
        conn.close()

        if df.empty:
            print("⚠️ Database is empty.")
            return

        # --- FIX: Explicitly tell Python the date format ---
        # Format handles "2025-12-28 23-56-25" (Hyphens in time)
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H-%M-%S', errors='coerce')
            
            # Remove any rows where date conversion failed (just in case)
            df = df.dropna(subset=['timestamp'])
            df.sort_values('timestamp', inplace=True)

        print(f"✅ Loaded {len(df)} records. Plotting...")

        plt.figure(figsize=(10, 5))
        if 'btc_price' in df.columns:
            plt.plot(df['timestamp'], df['btc_price'], label='Bitcoin (BTC)', color='orange')
        
        plt.title('Bitcoin Price Trend')
        plt.xlabel('Time')
        plt.ylabel('Price (INR)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        plt.savefig(IMAGE_NAME)
        print(f"✅ Graph saved as '{IMAGE_NAME}'")
        # plt.show() # Commented out show() to avoid display errors in some Linux terminals

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    plot_trends()