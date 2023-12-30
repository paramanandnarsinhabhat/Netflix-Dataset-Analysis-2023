import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn as sns
import matplotlib.pyplot as plt


cleaned_data_path = '/Users/paramanandbhat/Downloads/netflix_data_cleaned.csv'
netflix_df = pd.read_csv(cleaned_data_path)

netflix_df['Release Date'] = pd.to_datetime(netflix_df['Release Date'])
# Drop rows where 'Release Date' is NaN
netflix_df = netflix_df.dropna(subset=['Release Date'])

netflix_df['Year'] = netflix_df['Release Date'].dt.year.astype(int)


# Creating the box plot
plt.figure(figsize=(12, 6))
sns.boxplot(x='Year', y='Rating', data=netflix_df)
plt.title('Box Plot of Ratings by Year')
plt.xlabel('Year')
plt.ylabel('Rating')
plt.show()
