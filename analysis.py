import pandas as pd

# Load dataset
df = pd.read_csv("train.csv")

# Show first rows
print("First 5 rows:")
print(df.head())

# Basic info
print("\nDataset Info:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Example analysis (adjust based on dataset)
if 'Sales' in df.columns:
    print("\nTotal Sales:", df['Sales'].sum())

# Sales by Category
print("\nSales by Category:")
print(df.groupby('Category')['Sales'].sum())

# Sales by Region
print("\nSales by Region:")
print(df.groupby('Region')['Sales'].sum())