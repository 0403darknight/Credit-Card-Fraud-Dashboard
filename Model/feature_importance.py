import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    r"C:\Users\dhiks\OneDrive\Desktop\Credit Card Fraud Dashboard\Data\processed\fraud_cleaned.csv"
)

# Remove categorical column
df = df.drop("Transaction_Category", axis=1)

# Features
X = df.drop("Class", axis=1)

# Load trained model
model = joblib.load(
    r"C:\Users\dhiks\OneDrive\Desktop\Credit Card Fraud Dashboard\Model\saved_model.pkl"
)

# Calculate feature importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

# Sort by importance
importance = importance.sort_values(
    by="Importance",
    ascending=False
)

# Display top 10
top_10 = importance.head(10)

print("\nTop 10 Important Features:")
print(top_10)

# Save complete feature importance dataset
importance.to_csv(
    r"C:\Users\dhiks\OneDrive\Desktop\Credit Card Fraud Dashboard\Model\feature_importance.csv",
    index=False
)

print("\nfeature_importance.csv saved successfully!")

# Plot top 10
plt.figure(figsize=(10, 6))

plt.barh(
    top_10["Feature"][::-1],
    top_10["Importance"][::-1]
)

plt.title("Top 10 Feature Importances")
plt.xlabel("Importance")

plt.tight_layout()

plt.savefig(
    r"C:\Users\dhiks\OneDrive\Desktop\Credit Card Fraud Dashboard\Screenshots\model\feature_importance.png"
)

plt.show()