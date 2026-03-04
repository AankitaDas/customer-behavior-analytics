import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()
np.random.seed(42)

# Parameters
num_customers = 2000
num_transactions = 50000

# Customers table
customers = pd.DataFrame({
    "customer_id": range(1, num_customers + 1),
    "customer_name": [fake.name() for _ in range(num_customers)],
    "city": [fake.city() for _ in range(num_customers)],
    "age": np.random.randint(18, 65, num_customers),
    "gender": np.random.choice(["Male", "Female"], num_customers),
    "income_group": np.random.choice(
        ["Low", "Medium", "High"],
        num_customers,
        p=[0.4, 0.4, 0.2]
    )
})

# Transactions table
categories = ["Groceries", "Fuel", "Dining", "Travel", "Shopping", "Entertainment"]

transactions = pd.DataFrame({
    "transaction_id": range(1, num_transactions + 1),
    "customer_id": np.random.randint(1, num_customers + 1, num_transactions),
    "transaction_date": pd.to_datetime("2023-01-01") +
                        pd.to_timedelta(np.random.randint(0, 365, num_transactions), unit="D"),
    "category": np.random.choice(categories, num_transactions),
    "amount": np.round(np.random.exponential(scale=150, size=num_transactions), 2),
    "payment_type": np.random.choice(["Credit Card", "Debit Card", "UPI"], num_transactions)
})

# Save files
customers.to_csv("customers.csv", index=False)
transactions.to_csv("transactions.csv", index=False)

print("CSV files generated successfully!")
