import pandas as pd
import ast
import matplotlib.pyplot as plt

cleaned_data_path = '/Users/paramanandbhat/Downloads/netflix_data_cleaned.csv'
netflix_df = pd.read_csv(cleaned_data_path)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Rating', y='Hours Viewed', data=netflix_df)
plt.title('Scatter Plot of Ratings vs. Viewership Hours')
plt.xlabel('Rating')
plt.ylabel('Viewership Hours')
plt.show()

correlation = netflix_df['Rating'].corr(netflix_df['Hours Viewed'])
print("Correlation coefficient:", correlation)
