import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///consumer_spending.db")

# Revenue by Category
query1 = """
SELECT
    category,
    SUM(amount) as total_spend
FROM fact_transactions
GROUP BY category
"""

df1 = pd.read_sql(query1, engine)
print(df1)

# Monthly Spend Trend
query2 = """
SELECT
    strftime('%Y-%m', transaction_date) as month,
    SUM(amount) as monthly_spend
FROM fact_transactions
GROUP BY month
ORDER BY month
"""

df2 = pd.read_sql(query2, engine)
print(df2)

# Repeat Customers
query3 = """
SELECT
    customer_id,
    COUNT(transaction_id) as txn_count
FROM fact_transactions
GROUP BY customer_id
HAVING txn_count > 5
"""

df3 = pd.read_sql(query3, engine)
print(df3.head())
