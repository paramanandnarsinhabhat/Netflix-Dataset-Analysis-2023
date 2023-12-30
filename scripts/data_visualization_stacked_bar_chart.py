import pandas as pd

cleaned_data_path = '/Users/paramanandbhat/Downloads/netflix_data_cleaned.csv'
netflix_df = pd.read_csv(cleaned_data_path)

netflix_df['Release Date'] = pd.to_datetime(netflix_df['Release Date'])
# Drop rows where 'Release Date' is NaN
netflix_df = netflix_df.dropna(subset=['Release Date'])

netflix_df['Year'] = netflix_df['Release Date'].dt.year.astype(int)

