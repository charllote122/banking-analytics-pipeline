# 🏦 Banking Analytics Pipeline

## 📌 Overview
An end-to-end data analytics project simulating a retail bank. I extracted 2.8M+ rows of raw data, loaded it into PostgreSQL, analyzed it with SQL, and built an interactive Power BI dashboard to track liquidity and customer wealth.

## 🛠️ Tech Stack
*   **Python (pandas, SQLAlchemy):** ETL and data cleaning.
*   **PostgreSQL:** Data warehousing (10 tables).
*   **SQL:** Data exploration and business analysis.
*   **Power BI:** Data modeling (Star Schema) and visualization.

## 📊 Key Insights
*   **Liquidity:** Savings accounts hold the most capital (₹2.18B+).
*   **Top City:** Bengaluru holds the highest total account balances.
*   **Wealth:** Business Owners make up 7 of the top 10 richest customers.

## 📈 Dashboard Preview
![Banking Dashboard](dashboard.png)

## ⚙️ How to Run
1. Clone the repo.
2. Setup virtual environment: `python -m venv venv` and activate it.
3. Install requirements: `pip install pandas sqlalchemy "psycopg[binary]"`
4. Create a PostgreSQL database named `banking_db`.
5. Update your DB credentials in `python/import_data.py` and run it.
6. Open the `.pbix` file in Power BI to view the dashboard.
