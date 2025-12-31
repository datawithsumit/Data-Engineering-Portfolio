# 🐍 Python Development Portfolio

A collection of Python-based Data Engineering projects focusing on ETL pipelines, automation, cloud warehousing, and data simulation.

## 📂 Projects

### 1. 📈 Crypto Sniper Bot (Basic)
**Tech Stack:** Python, SQLite, CoinGecko API, Pandas
- A foundational ETL script that fetches live Bitcoin & Ethereum prices every 10 seconds.
- Uses a simple `while` loop with `time.sleep()` for scheduling.
- Stores raw logs in a structured SQL database.

### 2. 🛒 E-Commerce Data Simulator
![E-Commerce Analytics](02_Ecommerce_Simulator/ecommerce_analytics.png)
**Tech Stack:** Python, Random (Simulation), Pandas, SQLite
- A synthetic data generator that simulates 1,000+ customer orders for a fake retail store.
- Designed to stress-test data ingestion logic by generating random Cities, Products, and Prices.
- Includes an **Analytics Dashboard** that calculates Total Revenue, Top Cities, and Best-Selling Categories.

### 3. 🤖 MarketMood: Real-Time AI Sentiment Analysis
![MarketMood Dashboard](03_Sentiment_Dashboard/MarketMood_AI_Dashboard.png)
**Tech Stack:** Python, Streamlit, TextBlob (NLP), Plotly, Pandas
- A full-stack data application that processes live financial news feeds to gauge market sentiment.
- **Data Pipeline:** Simulates streaming text data ingestion.
- **AI/ML Engine:** Uses Natural Language Processing (TextBlob) to calculate polarity scores (Positive/Negative/Neutral) in real-time.
- **Visualization:** Renders a live-updating interactive dashboard with moving averages and trend lines using Plotly and Streamlit Session State.

### 4. 🚀 Crypto Sniper V2 (Airflow Pipeline)
![Bitcoin Price Trend](04_Crypto_Sniper_V2/crypto_price_trend.png)
**Tech Stack:** Apache Airflow, Python, SQLite, Matplotlib, Pandas
- An advanced version of the Crypto Sniper, orchestrated using **Apache Airflow DAGs**.
- **Orchestration:** Automates the extraction and loading process on a strict schedule.
- **Visualization:** Includes a specialized script (`visualize_crypto.py`) that generates trend graphs from the database.
- **Data Quality:** Implements robust error handling and API rate-limit management.

### 5. ❄️ E-Commerce Pipeline V2 (Snowflake Edition)
**Tech Stack:** Python, Snowflake (Cloud DW), Docker, Pandas

| **Raw Data Ingestion** | **Cloud Analytics** |
|:---:|:---:|
| ![Raw Data](05_Ecommerce_Snowflake_V2/snowflake_data_preview.png) | ![Sales Trends](05_Ecommerce_Snowflake_V2/snowflake_analytics.png) |

- **Enterprise Upgrade:** Migrated the local ETL pipeline to load synthetic sales data directly into **Snowflake** (Cloud Data Warehouse).
- **Cloud Architecture:** Implements a scalable batch insert strategy for handling large datasets in the cloud.
- **Analytics Ready:** Verified data integrity with SQL aggregations and utilized Snowflake's built-in visualization tools for reporting.

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/datawithsumit/Data-Engineering-Portfolio.git](https://github.com/datawithsumit/Data-Engineering-Portfolio.git)
   ```
2. **Navigate to a project folder: (Example: Sentiment Dashboard)**
   ```bash
   cd 03_Sentiment_Dashboard
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the specific project:**
   For MarketMood (AI Dashboard):
   ```bash
   streamlit run app.py
   ```
   For Crypto V2 (Airflow): (Ensure Airflow is running, or run the script manually)
   ```bash
   python crypto_sniper.py
   ```
   For E-Commerce Simulator (Local):
   ```bash
   python setup_ecommerce.py
   ```
   For E-Commerce V2 (Snowflake): (Requires Snowflake credentials)
   ```bash
   python main.py
   ```
   For E-Commerce V2 (Docker):
   ```bash
   docker build -t snowflake-ecommerce .
   docker run snowflake-ecommerce
   ```


