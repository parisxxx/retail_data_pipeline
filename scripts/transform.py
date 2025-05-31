import pandas as pd

def transform_data(df):
    """
    Cleans and transforms the sales data.
    
    - Drops rows with missing values
    - Converts 'Date' to datetime format
    - Adds 'Total' column (Quantity * Price)

    Args:
        df (DataFrame): Raw sales data

    Returns:
        DataFrame: Transformed data
    """
    if df.empty:
        print("Empty DataFrame received for transformation.")
        return df

    df = df.dropna()

    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    if 'Quantity' in df.columns and 'Price' in df.columns:
        df['Total'] = df['Quantity'] * df['Price']

    df = df.dropna()  # Drop any rows where 'Date' conversion failed

    return df

