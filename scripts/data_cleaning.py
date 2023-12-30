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

# Step 2: Standardize Text and Categorical Data
# For 'Available Globally?', convert 'Yes' to True and anything else to False
netflix_df['Available Globally?'] = netflix_df['Available Globally?'].map({'Yes': True, 'No': False})

# We will inspect the first few rows to ensure transformations have been done correctly
transformed_head = netflix_df.head()

# We also check for any null values which may have been introduced during conversion
missing_values_after_conversion = netflix_df.isnull().sum()

print(transformed_head)
print(missing_values_after_conversion)

# Step 3: Handle Missing Values
# For numeric columns with very few missing values, we'll fill them with the median
numeric_columns = ['Hours Viewed', 'Number of Ratings', 'Rating']
for column in numeric_columns:
    median_value = netflix_df[column].median()
    netflix_df[column].fillna(median_value, inplace=True)
# Since 'Release Date' has a significant number of missing values, we'll leave them as NaN for now
# They could be imputed later if they are required for time-series analysis
# Step 4: Clean Genre Column
# We'll define a function to parse the 'Genre' column into actual lists
def parse_genre(genre_str):
    # Removing quotes and square brackets
    genre_str = genre_str.strip("[]")
    # Splitting the string into a list at commas not followed by a space (to avoid splitting on commas within genres)
    genres = [genre.strip("' ") for genre in genre_str.split(",")]
    return genres

# Apply the parsing function to the 'Genre' column
netflix_df['Genre'] = netflix_df['Genre'].apply(parse_genre)

# Step 5: Validate Data
# Ensure 'Rating' is within the 0-10 range
netflix_df = netflix_df[(netflix_df['Rating'] >= 0) & (netflix_df['Rating'] <= 10)]

## Ensure 'Hours Viewed' and 'Number of Ratings' are non-negative
netflix_df = netflix_df[(netflix_df['Hours Viewed'] >= 0) & (netflix_df['Number of Ratings'] >= 0)]

# Check the transformations and the data
transformed_genre_head = netflix_df.head()
transformed_genre_head, netflix_df.isnull().sum()

# Additional preprocessing steps:

# Step 6: Extract Additional Information from 'Release Date'
# We'll extract year, month, and day as new columns, which can be useful for time-based analysis later.
netflix_df['Year'] = netflix_df['Release Date'].dt.year
netflix_df['Month'] = netflix_df['Release Date'].dt.month
netflix_df['Day'] = netflix_df['Release Date'].dt.day


