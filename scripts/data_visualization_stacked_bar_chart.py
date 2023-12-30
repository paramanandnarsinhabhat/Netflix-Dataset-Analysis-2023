import pandas as pd
import ast
import matplotlib.pyplot as plt

cleaned_data_path = '/Users/paramanandbhat/Downloads/netflix_data_cleaned.csv'
netflix_df = pd.read_csv(cleaned_data_path)

netflix_df['Release Date'] = pd.to_datetime(netflix_df['Release Date'])
# Drop rows where 'Release Date' is NaN
netflix_df = netflix_df.dropna(subset=['Release Date'])

netflix_df['Year'] = netflix_df['Release Date'].dt.year.astype(int)

netflix_df['Genre'] = netflix_df['Genre'].apply(ast.literal_eval)

# Take only the first genre from the list to simplify
netflix_df['Primary Genre'] = netflix_df['Genre'].apply(lambda x: x[0] if x else 'Unknown')

# Now aggregate by year and primary genre
genre_yearly = netflix_df.groupby(['Year', 'Primary Genre']).size().unstack(fill_value=0)

# Optionally, you can focus on the top N genres
top_genres = netflix_df['Primary Genre'].value_counts().nlargest(10).index
genre_yearly_top = genre_yearly[top_genres]


# Plotting the simplified stacked bar chart
plt.figure(figsize=(12, 8))
genre_yearly_top.plot(kind='bar', stacked=True, figsize=(12, 8))
plt.title('Stacked Bar Chart of Top Genres Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.legend(title='Primary Genre')
plt.show()
