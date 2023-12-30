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

#Step 3 : Handle missing values
netflix_df = handle_missing_values(netflix_df)

#Step 4: Validate Data Function
netflix_df = validate_data(netflix_df)

#Step 5 : Extract the date components to Extract Additional Information Function
netflix_df = extract_date_components(netflix_df)

#Step 6 : Outlier Detection Function

netflix_df = detect_outliers(netflix_df, 'Rating')

