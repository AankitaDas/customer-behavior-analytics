import pandas as pd
from sqlalchemy import create_engine

# Create SQLite DB
engine = create_engine("sqlite:///consumer_spending.db")

# Load CSV files
customers = pd.read_csv("customers.csv")
transactions = pd.read_csv("transactions.csv")

# Push to SQL
customers.to_sql("dim_customers", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)

print("Data loaded into SQLite database successfully!")
