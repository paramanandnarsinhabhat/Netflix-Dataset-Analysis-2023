import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.data_utils import load_data

file_path = '/Users/paramanandbhat/Downloads/total_netflix_2023 new.csv'

df_exploration = load_data(file_path)
print(df_exploration.head())