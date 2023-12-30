import pandas as pd
cleaned_data_path = '/Users/paramanandbhat/Downloads/netflix_data_cleaned.csv'
netflix_df = pd.read_csv(cleaned_data_path)

# Convert 'Release Date' to datetime and extract the year
netflix_df['Release Date'] = pd.to_datetime(netflix_df['Release Date'])
netflix_df['Year'] = netflix_df['Release Date'].dt.year

# Example of taking the first genre from a list as the primary genre
# Simplify the Genre Data
import ast  
netflix_df['Genre'] = netflix_df['Genre'].apply(ast.literal_eval)  # Converts string to list
netflix_df['Primary Genre'] = netflix_df['Genre'].apply(lambda x: x[0] if x else 'Unknown')

#Aggregate the Data by Year and Genre
genre_yearly_counts = netflix_df.groupby(['Year', 'Primary Genre']).size()




# Find the Most Popular Genre Each Year
most_popular_genre_by_year = genre_yearly_counts.unstack().idxmax(axis=1)
most_popular_genre_by_year.index = most_popular_genre_by_year.index.astype(int)

# Create a frequency table of genres
genre_frequency = most_popular_genre_by_year.value_counts()

print(genre_frequency)

# Plotting the frequency table
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
genre_frequency.plot(kind='bar', color='skyblue')
plt.title('Frequency of Most Popular Genre by Year')
plt.xlabel('Genre')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()

