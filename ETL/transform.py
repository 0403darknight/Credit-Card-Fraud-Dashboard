import pandas as pd
import numpy as np
import os

# Read raw data
df = pd.read_csv(
    r"C:\Users\dhiks\OneDrive\Desktop\Credit Card Fraud Dashboard\Data\creditcard.csv"
)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Create log-transformed amount feature
df["Amount_Log"] = np.log1p(df["Amount"])

# Create transaction category feature
df["Transaction_Category"] = pd.cut(
    df["Amount"],
    bins=[-0.01, 50, 200, 1000, 5000, float("inf")],
    labels=[
        "Low",
        "Medium",
        "High",
        "Very High",
        "Extreme"
    ],
    include_lowest=True
)

# Create processed folder if it doesn't exist
os.makedirs(
    r"C:\Users\dhiks\OneDrive\Desktop\Credit Card Fraud Dashboard\Data\processed",
    exist_ok=True
)


df.to_csv(
    r"C:\Users\dhiks\OneDrive\Desktop\Credit Card Fraud Dashboard\Data\processed\fraud_cleaned.csv",
    index=False
)

print("Data transformed and saved successfully!")