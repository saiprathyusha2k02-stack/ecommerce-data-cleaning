import pandas as pd
df = pd.read_csv("data/ecommerce_data.csv")
print("Original Data:")
print(df)
import pandas as pd

df = pd.read_csv("data/ecommerce_data.csv")

print("Original Data:")
print(df)
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())
df["Age"] = df["Age"].fillna(df["Age"].median())
print("\nDuplicate Rows:")
print(df.duplicated().sum())
df = df.drop_duplicates()
print("\nDuplicates After Cleaning:")
print(df.duplicated().sum())
print("\nDuplicates After Cleaning:")
print(df.duplicated().sum())
df["City"] = df["City"].str.strip().str.title()
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
print("\nFinal Missing Values:")
print(df.isnull().sum())

print("\nFinal Duplicate Count:")
print(df.duplicated().sum())

print("\nCleaned Data:")
print(df)
df.to_csv("data/cleaned_ecommerce_data.csv", index=False)

print("\nCleaned dataset saved successfully!")