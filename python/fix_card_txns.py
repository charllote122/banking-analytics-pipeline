import pandas as pd
from sqlalchemy import create_engine

# 1. Connect
DB_USER = "postgres"
DB_PASS = "postgres"  
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "banking_db"
engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# 2. Read only the failing CSV
print("Reading card_transactions.csv...")
df = pd.read_csv("data/raw/card_transactions.csv")

# 3. Convert the date
df["txn_date"] = pd.to_datetime(df["txn_date"], errors="coerce")

# 4. Import
print("Importing to PostgreSQL...")
df.to_sql("card_transactions", engine, if_exists="append", index=False)

print(f"✅ Success! Imported {len(df)} rows into card_transactions.")
