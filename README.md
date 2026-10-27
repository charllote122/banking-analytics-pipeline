# 🏦 Banking Transactions Analytics Pipeline

## 📌 Project Overview
This is an end-to-end data analytics project simulating a retail banking environment. The goal was to extract, clean, and load over 2.8 million rows of raw banking data into a relational database, perform SQL analysis to answer business questions, and build an interactive Power BI dashboard to track bank liquidity and customer wealth distribution.

## 🛠️ Tech Stack
*   **Python (pandas, SQLAlchemy):** Data extraction, cleaning (handling datatype mismatches), and loading (ETL).
*   **PostgreSQL:** Relational database for data warehousing (10 interconnected tables).
*   **SQL:** Data exploration, `JOIN`s, and aggregations to answer business questions.
*   **Power BI:** Data modeling (Star Schema) and interactive dashboarding.

## 📂 Dataset Structure
The database consists of 10 tables representing a banking ecosystem, including:
*   `customers`: Demographics, income, and credit scores.
*   `accounts`: Bank accounts, balances, and account types.
*   `transactions` & `card_transactions`: Day-to-day money movement (over 2.8M rows).
*   `loans` & `loan_payments`: Lending data and risk metrics.
*   `branches`, `employees`, `cards`, `support_tickets`.

## 📊 Key Business Insights Found
Using SQL to query the PostgreSQL database, I discovered the following insights:
*   **Liquidity:** Savings accounts hold the largest portion of the bank's capital (over ₹2.18 Billion), followed by Current accounts.
*   **Top Cities:** Bengaluru is the highest-value city for the bank, holding the most total account balances.
*   **Wealth Concentration:** Business Owners make up the majority (7 out of 10) of the bank's richest customers. 

## 📈 Interactive Dashboard
The Power BI dashboard allows executives to filter by account type to see total balances by city, top-level KPIs (Total Balance, Average Balance), and visualizes the bank's liquidity.

*(Make sure you save your dashboard screenshot as `dashboard.png` in this same folder!)*
![Banking Dashboard](dashboard.png)

## ⚙️ How to Run This Project Locally

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/Banking-Transactions-Analytics.git
cd Banking-Transactions-Analytics

2. Set up a virtual environment

python -m venv venv
# On Windows Git Bash:
source venv/Scripts/activate
# On Mac/Linux:
source venv/bin/activate