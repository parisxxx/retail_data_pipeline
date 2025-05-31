# Directory: retail_data_pipeline
# File: main.py

from scripts.extract import extract_data, A
from scripts.transform import transform_data
from scripts.load import load_data

if __name__ == "__main__":
    print("Starting ETL pipeline...")

    raw_df = extract_data("data/raw_sales_data.csv")
    print("Data extracted.")

    transformed_df = transform_data(raw_df)
    print("Data transformed.")

    load_data(transformed_df, "database/retail.db")
    print("Data loaded into database.")

# File: scripts/extract.py
import pandas as pd

def extract_data(filepath):
    return pd.read_csv(filepath)

# File: scripts/transform.py
import pandas as pd

def transform_data(df):
    # Drop rows with any missing values
    df = df.dropna()
    
    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Add a new column 'Total' = Quantity * Price
    df['Total'] = df['Quantity'] * df['Price']

    return df

# File: scripts/load.py
import sqlite3

def load_data(df, db_path):
    conn = sqlite3.connect(db_path)
    df.to_sql("sales", conn, if_exists="replace", index=False)
    conn.close()

# File: data/raw_sales_data.csv
# Sample data (put this in a CSV file manually)
# OrderID,Product,Region,Quantity,Price,Date
# 1001,Apples,West,10,1.2,2023-01-15
# 1002,Bananas,East,5,0.8,2023-01-16
# 1003,Oranges,North,8,1.0,2023-01-17
# 1004,Apples,South,12,1.3,2023-01-18
# 1005,Bananas,West,7,0.9,2023-01-19
