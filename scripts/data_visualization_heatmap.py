import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cleaned_data_path = '/Users/paramanandbhat/Downloads/netflix_data_cleaned.csv'
netflix_df = pd.read_csv(cleaned_data_path)

# Convert 'Release Date' to datetime and extract year and month
netflix_df['Release Date'] = pd.to_datetime(netflix_df['Release Date'])
netflix_df['Year'] = netflix_df['Release Date'].dt.year
netflix_df['Month'] = netflix_df['Release Date'].dt.month

# Create a pivot table for the heatmap
pivot_table = netflix_df.pivot_table(index='Year', columns='Month', values='Title', aggfunc='count')

# Plotting the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, cmap='coolwarm', fmt='g')
plt.title('Heatmap of Netflix Titles Released by Month and Year')
plt.xlabel('Month')
plt.ylabel('Year')
plt.show()

