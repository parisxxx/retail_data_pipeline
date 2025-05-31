import sqlite3

def load_data(df, db_path):
    """
    Loads the transformed data into a SQLite database.

    Args:
        df (DataFrame): Transformed sales data
        db_path (str): Path to SQLite database
    """
    if df.empty:
        print("No data to load.")
        return

    try:
        conn = sqlite3.connect(db_path)
        df.to_sql("sales", conn, if_exists="replace", index=False)
        conn.close()
        print(f"Data successfully loaded into {db_path}")
    except Exception as e:
        print(f"Error loading data into database: {e}")
