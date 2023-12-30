import pandas as pd

def load_data(file_path):
    """Load data from a CSV file into a DataFrame."""
    return pd.read_csv(file_path)

