import pandas as pd

def parse_genre(genre_str):
    genre_str = genre_str.strip("[]")
    return [genre.strip("' ") for genre in genre_str.split(",")]

def load_data(file_path):
    """Load data from a CSV file into a DataFrame."""
    return pd.read_csv(file_path)

def convert_data_types(df):
    df['Release Date'] = pd.to_datetime(df['Release Date'], errors='coerce')
    df['Hours Viewed'] = pd.to_numeric(df['Hours Viewed'], errors='coerce')
    df['Number of Ratings'] = pd.to_numeric(df['Number of Ratings'], errors='coerce')
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
    return df

def standardize_and_clean_data(df):
    df['Available Globally?'] = df['Available Globally?'].map({'Yes': True, 'No': False})
    df['Genre'] = df['Genre'].apply(parse_genre)
    df['Key Words'] = df['Key Words'].str.strip()
    df['Description'] = df['Description'].str.strip()
    return df





