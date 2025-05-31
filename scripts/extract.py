import pandas as pd

def extract_data(filepath):
    """
    Reads a CSV file and returns a pandas DataFrame.
    
    Args:
        filepath (str): Path to the CSV file.

    Returns:
        DataFrame: Loaded data.
    """
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error reading the file: {e}")
        return pd.DataFrame()
