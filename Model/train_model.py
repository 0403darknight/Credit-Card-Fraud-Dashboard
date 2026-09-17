import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE

# ==========================
# LOAD DATA
# ==========================

df = pd.read_csv(
    r"C:\Users\dhiks\OneDrive\Desktop\Credit Card Fraud Dashboard\Data\processed\fraud_cleaned.csv"
)

# Remove categorical feature for baseline model
df = df.drop("Transaction_Category", axis=1)

# ==========================
# FEATURES & TARGET
# ==========================

X = df.drop("Class", axis=1)
y = df["Class"]

# ==========================
# TRAIN TEST SPLIT
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ==========================
# HANDLE CLASS IMBALANCE
# ==========================

print("Before SMOTE:")
print(y_train.value_counts())

smote = SMOTE(random_state=42)

X_train_smote, y_train_smote = smote.fit_resample(
    X_train,
    y_train
)

print("\nAfter SMOTE:")
print(y_train_smote.value_counts())

# ==========================
# RANDOM FOREST MODEL
# ==========================

rf = RandomForestClassifier(
    n_estimators=200,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)

rf.fit(X_train_smote, y_train_smote)

# ==========================
# EVALUATION
# ==========================

y_pred = rf.predict(X_test)

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# ==========================
# SAVE MODEL
# ==========================

joblib.dump(
    rf,
    r"C:\Users\dhiks\OneDrive\Desktop\Credit Card Fraud Dashboard\Model\saved_model.pkl"
)

print("\nModel saved successfully!")