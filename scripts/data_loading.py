import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.data_utils import load_data

file_path = '/Users/paramanandbhat/Downloads/total_netflix_2023 new.csv'

netflix_df = load_data(file_path)


# Display the first few rows and summary information about the dataset
initial_head = netflix_df.head()
summary_info = netflix_df.info()
print(initial_head)
print(summary_info)
