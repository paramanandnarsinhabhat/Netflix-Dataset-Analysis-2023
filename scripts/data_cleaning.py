import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.data_utils import load_data,convert_data_types,standardize_and_clean_data

file_path = '/Users/paramanandbhat/Downloads/total_netflix_2023 new.csv'

netflix_df = load_data(file_path)
# Step 1: Convert Data Types
netflix_df = convert_data_types(netflix_df)



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
netflix_df = standardize_and_clean_data(netflix_df)

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

# For rows with a missing 'Release Date', these new columns will also have NaN values.
# We'll fill these NaN values with a placeholder (e.g., -1) to indicate missing data.
netflix_df['Year'].fillna(-1, inplace=True)
netflix_df['Month'].fillna(-1, inplace=True)
netflix_df['Day'].fillna(-1, inplace=True)


# Step 7: Text Field Cleaning 
# As the 'Key Words' and 'Description' fields look relatively clean, we will perform simple whitespace stripping.
netflix_df['Key Words'] = netflix_df['Key Words'].str.strip()
netflix_df['Description'] = netflix_df['Description'].str.strip()

# Step 8: Check for Outliers 
# We can perform a simple check for outliers in the numerical data using the IQR (Interquartile Range) method.
Q1 = netflix_df['Rating'].quantile(0.25)
Q3 = netflix_df['Rating'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out the outliers
outliers = netflix_df[(netflix_df['Rating'] < lower_bound) | (netflix_df['Rating'] > upper_bound)]
non_outliers = netflix_df[(netflix_df['Rating'] >= lower_bound) & (netflix_df['Rating'] <= upper_bound)]

# We now have a DataFrame without outliers in 'Rating'
netflix_df_cleaned = non_outliers

# Show the number of outliers detected and the first few rows of the cleaned dataframe
num_outliers = outliers.shape[0]
cleaned_head = netflix_df_cleaned.head()

num_outliers, cleaned_head

