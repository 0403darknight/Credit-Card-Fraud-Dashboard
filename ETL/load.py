import sqlite3
import pandas as pd

conn = sqlite3.connect('fraud.db')

df = pd.read_csv(
    'data/processed/fraud_cleaned.csv'
)

df.to_sql(
    'transactions',
    conn,
    if_exists='replace',
    index=False
)

conn.close()