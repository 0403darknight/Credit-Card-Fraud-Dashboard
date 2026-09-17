import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    roc_auc_score,
    RocCurveDisplay
)

# ==========================
# LOAD DATA
# ==========================

df = pd.read_csv(
    r"C:\Users\dhiks\OneDrive\Desktop\Credit Card Fraud Dashboard\Data\processed\fraud_cleaned.csv"
)

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
# LOAD MODEL
# ==========================

model = joblib.load(
    r"C:\Users\dhiks\OneDrive\Desktop\Credit Card Fraud Dashboard\Model\saved_model.pkl"
)

# ==========================
# PREDICTIONS
# ==========================

y_pred = model.predict(X_test)

# ==========================
# CLASSIFICATION REPORT
# ==========================

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# ==========================
# CONFUSION MATRIX
# ==========================

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

ConfusionMatrixDisplay.from_predictions(
    y_test,
    y_pred
)

plt.title("Confusion Matrix")

plt.savefig(
    r"C:\Users\dhiks\OneDrive\Desktop\Credit Card Fraud Dashboard\Screenshots\model\confusion_matrix.png"
)

plt.show()

# ==========================
# ROC AUC SCORE
# ==========================

y_prob = model.predict_proba(X_test)[:, 1]

roc_score = roc_auc_score(
    y_test,
    y_prob
)

print("\nROC-AUC Score:", round(roc_score, 4))

# ==========================
# ROC CURVE
# ==========================

RocCurveDisplay.from_predictions(
    y_test,
    y_prob
)

plt.title("ROC Curve")

plt.savefig(
    r"C:\Users\dhiks\OneDrive\Desktop\Credit Card Fraud Dashboard\Screenshots\model\roc_curve.png"
)

plt.show()