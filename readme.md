# 🐍 Python Data Engineering Portfolio

A collection of Python-based Data Engineering projects focusing on ETL pipelines, automation, and data simulation.

## 📂 Projects

### 1. 📈 Crypto Sniper Bot
**Tech Stack:** Python, SQLite, CoinGecko API, Pandas
- A real-time data ingestion pipeline that fetches live Bitcoin & Ethereum prices every 10 seconds.
- Stores raw logs in a structured SQL database.
- Performs basic analytics to calculate the BTC/ETH price ratio.

### 2. 🛒 E-Commerce Data Simulator
**Tech Stack:** Python, Random (Simulation), Pandas, SQLite
- A synthetic data generator that simulates 1,000+ customer orders for a fake retail store.
- Designed to stress-test data ingestion logic by generating random Cities, Products, and Prices.
- Includes an **Analytics Dashboard** that calculates Total Revenue, Top Cities, and Best-Selling Categories.

### 3. 🤖 MarketMood: Real-Time AI Sentiment Analysis
**Tech Stack:** Python, Streamlit, TextBlob (NLP), Plotly, Pandas
- A full-stack data application that processes live financial news feeds to gauge market sentiment.
- **Data Pipeline:** Simulates streaming text data ingestion.
- **AI/ML Engine:** Uses Natural Language Processing (TextBlob) to calculate polarity scores (Positive/Negative/Neutral) in real-time.
- **Visualization:** Renders a live-updating interactive dashboard with moving averages and trend lines using Plotly and Streamlit Session State.


## 🚀 How to Run
1. Clone the repository.
2. Navigate to the project folder (e.g., `02_Ecommerce_Simulator`).
3. Run the setup script to generate data:
   ```bash
   python setup_ecommerce.py
4. Run the dashboard to see insights: python dashboard.py
4. Run the setup script to generate data:
   ```bash
   python setup_ecommerce.py
