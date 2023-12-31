import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.data_utils import load_data,convert_data_types,standardize_and_clean_data,handle_missing_values,validate_data,extract_date_components,detect_outliers

file_path = '/Users/paramanandbhat/Downloads/total_netflix_2023 new.csv'

netflix_df = load_data(file_path)
# Step 1: Convert Data Types
netflix_df = convert_data_types(netflix_df)

# Step 2: Standardize Text and Categorical Data
netflix_df = standardize_and_clean_data(netflix_df)


#Step 3 : Extract the date components to Extract Additional Information Function
netflix_df = extract_date_components(netflix_df)
#Step 4 : Handle missing values
netflix_df = handle_missing_values(netflix_df)

#Step 5: Validate Data Function
netflix_df = validate_data(netflix_df)


#Step 6 : Outlier Detection Function

netflix_df = detect_outliers(netflix_df, 'Rating')

netflix_df_cleaned = netflix_df

# Step 7 : Save the cleaned data to a CSV file
cleaned_data_path = '/Users/paramanandbhat/Downloads/netflix_data_cleaned.csv'
netflix_df_cleaned.to_csv(cleaned_data_path, index=False)

# Return the path to the saved cleaned data file
print(cleaned_data_path)