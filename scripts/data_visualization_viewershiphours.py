import pandas as pd
import ast

cleaned_data_path = '/Users/paramanandbhat/Downloads/netflix_data_cleaned.csv'
netflix_df = pd.read_csv(cleaned_data_path)

netflix_df['Genre'] = netflix_df['Genre'].apply(ast.literal_eval)  # Converts string to list
netflix_df['Primary Genre'] = netflix_df['Genre'].apply(lambda x: x[0] if isinstance(x, list) and x else 'Unknown')

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 7))
sns.boxplot(x='Primary Genre', y='Hours Viewed', data=netflix_df)
plt.title('Distribution of Viewership Hours by Genre')
plt.xlabel('Genre')
plt.ylabel('Viewership Hours')
plt.xticks(rotation=45)
plt.show()