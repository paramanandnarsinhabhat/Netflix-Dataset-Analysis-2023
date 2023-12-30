import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cleaned_data_path = '/Users/paramanandbhat/Downloads/netflix_data_cleaned.csv'
netflix_df = pd.read_csv(cleaned_data_path)

#Convert 'Release Date' to Datetime
netflix_df['Release Date'] = pd.to_datetime(netflix_df['Release Date'])
#Extract the Year
netflix_df['Year'] = netflix_df['Release Date'].dt.year
#Aggregate Data by Year
titles_per_year = netflix_df.groupby('Year').size()
titles_per_year.index = titles_per_year.index.astype(int)
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

# Plotting
plt.figure(figsize=(12, 6))
ax = titles_per_year.plot(kind='bar', color='skyblue')
plt.title('Total Titles Released Each Year on Netflix')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.xticks(rotation=45)

# Adding the text on top of each bar
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

plt.show()


