# Directory: retail_data_pipeline
# File: main.py

from scripts.extract import extract_data
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

