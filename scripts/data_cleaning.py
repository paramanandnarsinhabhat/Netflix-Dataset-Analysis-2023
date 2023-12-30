import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.data_utils import load_data

file_path = '/Users/paramanandbhat/Downloads/total_netflix_2023 new.csv'

netflix_df = load_data(file_path)

# Step 1: Convert Data Types

# Convert 'Release Date' to datetime
netflix_df['Release Date'] = pd.to_datetime(netflix_df['Release Date'], errors='coerce')

# Convert 'Hours Viewed', 'Number of Ratings', and 'Rating' to numeric types
netflix_df['Hours Viewed'] = pd.to_numeric(netflix_df['Hours Viewed'], errors='coerce')
netflix_df['Number of Ratings'] = pd.to_numeric(netflix_df['Number of Ratings'], errors='coerce')
netflix_df['Rating'] = pd.to_numeric(netflix_df['Rating'], errors='coerce')
