import pandas as pd
import os

# Path to raw datasets
DATA_PATH = "D:\\Projects\\mutual_fund_analysis\\data\\raw"

# Get all CSV files
csv_files = [file for file in os.listdir(DATA_PATH) if file.endswith(".csv")]

print(f"\nTotal CSV Files Found: {len(csv_files)}")

# Loop through files
for file in csv_files:

    print("\n" + "="*60)
    print(f"FILE NAME: {file}")

    file_path = os.path.join(DATA_PATH, file)

    try:
        df = pd.read_csv(file_path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

    except Exception as e:
        print(f"Error reading {file}: {e}")

print("\n" + "="*60)
print("FUND MASTER EXPLORATION")

# Load fund master dataset
fund_master = pd.read_csv("D:\\Projects\\mutual_fund_analysis\\data\\raw\\01_fund_master.csv")

print(fund_master.columns)

# Unique fund houses
print("\nUnique Fund Houses:")
print(fund_master['fund_house'].unique())

# Categories
print("\nCategories:")
print(fund_master['category'].unique())

# Subcategories
print("\nSubcategories:")
print(fund_master['sub_category'].unique())

# Risk grades
print("\nRisk Grades:")
print(fund_master['risk_category'].unique())


print("\n" + "="*60)
print("AMFI CODE VALIDATION")

# Load NAV history
nav_history = pd.read_csv("D:\\Projects\\mutual_fund_analysis\\data\\raw\\02_nav_history.csv")

# Compare codes
master_codes = set(fund_master['amfi_code'])
nav_codes = set(nav_history['amfi_code'])

missing_codes = master_codes - nav_codes

print("\nMissing AMFI Codes:")
print(missing_codes)

print(f"\nTotal Missing Codes: {len(missing_codes)}")