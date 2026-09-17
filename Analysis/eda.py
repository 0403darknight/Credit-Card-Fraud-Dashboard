import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Data/processed/fraud_cleaned.csv")

print(df.head())
print(df.info())
print(df.describe())

sns.countplot(x="Class", data=df)

plt.title("Fraud vs Non-Fraud Transactions")

plt.show()

plt.figure(figsize=(10,5))

sns.histplot(
    df["Amount"],
    bins=50
)

plt.title("Transaction Amount Distribution")

plt.show()

sns.boxplot(
    x="Class",
    y="Amount",
    data=df
)

plt.title("Fraud vs Genuine Transaction Amounts")

plt.show()

sns.countplot(
    x="Transaction_Category",
    data=df
)

plt.xticks(rotation=45)

plt.show()

fraud_by_category = pd.crosstab(
    df["Transaction_Category"],
    df["Class"]
)

fraud_by_category.plot(
    kind="bar",
    stacked=True
)

plt.title("Fraud by Transaction Category")

plt.show()

plt.figure(figsize=(14,10))

sns.heatmap(
    df.select_dtypes(include='number').corr(),
    cmap='coolwarm'
)

plt.show()