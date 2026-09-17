-- Verify Total Records
SELECT COUNT(*) AS Total_Transactions
FROM fraud_cleaned;

-- Fraud vs Non-Fraud Distribution
SELECT
    Class,
    COUNT(*) AS Transaction_Count
FROM fraud_cleaned
GROUP BY Class;

-- Fraud Rate (%)
SELECT
ROUND(
    100.0 * SUM(Class) / COUNT(*),
    3
) AS Fraud_Rate_Percent
FROM fraud_cleaned;

-- Transaction Category Analysis
SELECT
    Transaction_Category,
    COUNT(*) AS Total_Transactions,
    SUM(Class) AS Fraud_Count
FROM fraud_cleaned
GROUP BY Transaction_Category;

-- Average Transaction Amount
SELECT
ROUND(AVG(Amount),2) AS Avg_Transaction_Amount
FROM fraud_cleaned;

-- Average Fraud Amount
SELECT
MAX(Amount) AS Highest_Fraud_Amount
FROM fraud_cleaned
WHERE Class = 1;

-- Maximum Fraud Transaction
SELECT
MAX(Amount) AS Highest_Fraud_Amount
FROM fraud_cleaned
WHERE Class = 1;

-- Top 10 Fraud Transactions
SELECT
    Amount,
    Time
FROM fraud_cleaned
WHERE Class = 1
ORDER BY Amount DESC
LIMIT 10;

-- Fraud Count by Transaction Category
SELECT
    Transaction_Category,
    SUM(Class) AS Fraud_Count
FROM fraud_cleaned
GROUP BY Transaction_Category
ORDER BY Fraud_Count DESC;

-- Fraud Percentage by Category
SELECT
    Transaction_Category,
    COUNT(*) AS Total_Transactions,
    SUM(Class) AS Fraud_Count,
    ROUND(
        100.0 * SUM(Class) / COUNT(*),
        2
    ) AS Fraud_Percentage
FROM fraud_cleaned
GROUP BY Transaction_Category;