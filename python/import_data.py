import pandas as pd
from sqlalchemy import create_engine
import os

# --- 1. CONFIGURATION ---
DB_USER = "postgres"
DB_PASS = "postgres"  
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "banking_db"

# Note: I added +psycopg2 here to fix the earlier driver issue
engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

data_folder = "data/raw"

print("Starting import process...\n")

for file in os.listdir(data_folder):
    if file.endswith(".csv"):
        table_name = file.replace(".csv", "")
        file_path = os.path.join(data_folder, file)

        print(f"Loading {file} into {table_name}...")

        try:
            # Read CSV
            df = pd.read_csv(file_path)

            # --- NEW FIX: AUTOMATICALLY CONVERT DATE COLUMNS ---
            # Look at any column with the word "date" in its name and convert it to a real Date
            for col in df.columns:
                if "date" in col.lower():
                    df[col] = pd.to_datetime(df[col], errors="coerce")

            # Import to PostgreSQL
            df.to_sql(table_name, engine, if_exists="append", index=False)

            print(f"✅ Success! Imported {len(df)} rows.\n")
        except Exception as e:
            print(f"❌ ERROR importing {table_name}: {e}\n")

print("🎉 ALL TABLES IMPORTED!")
