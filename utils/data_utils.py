import pandas as pd

def load_data(file_path):
    """Load data from a CSV file into a DataFrame."""
    return pd.read_csv(file_path)

def convert_data_types(df):
    df['Release Date'] = pd.to_datetime(df['Release Date'], errors='coerce')
    df['Hours Viewed'] = pd.to_numeric(df['Hours Viewed'], errors='coerce')
    df['Number of Ratings'] = pd.to_numeric(df['Number of Ratings'], errors='coerce')
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
    return df






