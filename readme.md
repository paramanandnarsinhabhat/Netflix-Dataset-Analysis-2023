
# Netflix Dataset Analysis 

## Project Overview
This project focuses on analyzing the Netflix dataset for the year 2010 to 2023. The analysis covers various aspects such as viewership trends, ratings, and content preferences globally. The goal is to derive meaningful insights that can help understand viewer behavior and preferences.

## Data Source
The dataset used in this project is titled `total_netflix_2023.csv` and includes information on various Netflix titles, their release dates, viewership hours, ratings, and other relevant details.

## Repository Structure
```
Netflix-Dataset-Analysis-2023/
│
├── data/
│   ├── raw/
│   │   └── total_netflix_2023.csv
│   └── processed/
│       └── netflix_data_cleaned.csv
│
├── notebooks/
│   └── Netflix_Data_Analysis.ipynb
│
├── scripts/
│   ├── data_preprocessing.py
│   └── analysis_helpers.py
│
├── results/
│   ├── figures/
│   │   ├── viewership_trends.png
│   │   └── rating_distribution.png
│   └── summary_report.md
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Tools and Technologies
- Python
- Pandas and NumPy for data manipulation
- Matplotlib and Seaborn for data visualization
- Jupyter Notebook for interactive analysis

## Installation and Usage
1. Clone the repository:
   ```
   git clone https://github.com/[your-username]/Netflix-Dataset-Analysis-2023.git
   ```
2. Navigate to the project directory:
   ```
   cd Netflix-Dataset-Analysis-2023
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run Jupyter Notebook to open the analysis:
   ```
   jupyter notebook
   ```

## Analysis Highlights
- Based on the bar chart provided, which appears to show the total number of titles released on Netflix each year, here are some observations:

Analyzing the Evolution of Content Volume on Netflix: A Decade of Expansion and a Pivotal Decline in 2023

1. **Growth Trend**: There is a noticeable growth trend in the number of titles released each year from 2010 through 2021. This suggests an aggressive expansion of content on the platform over the years.

2. **Peak in 2021**: The peak number of releases occurred in 2021, with 2839 titles released. This could be indicative of a strategic push for more content or an accumulation of titles due to external factors (like production delays in previous years that may have caused a surge when released).

3. **Sharp Decline in 2023**: There is a sharp decline in the number of titles released in 2023, dropping to 991. This could be due to several reasons:
   - Data for 2023 might be incomplete, especially if the data was collected partway through the year.
   - A change in business strategy or content curation policy at Netflix.
   - External factors affecting content production and release schedules (e.g., global events, industry-wide changes).

4. **Steady Increase Pre-Peak**: Leading up to 2021, there was a steady increase each year except for 2019, where the count slightly decreased from 2086 in 2018 to 1777 in 2019. This decrease could be a result of changing market strategies or natural variations in content production cycles.

5. **Possible Saturation Point**: The peak in 2021 followed by a decline could suggest a saturation point had been reached, where the platform began focusing on content quality over quantity, or perhaps market saturation led to a strategic reduction.

6. **Initial Years**: The very low numbers in the initial years (2010-2013) indicate the early stages of Netflix's content library when it was probably transitioning from a DVD rental service to a streaming platform.

 
 Stability in Viewer Ratings on Netflix Over Fourteen Years


1. **Consistent Median Ratings**: The median ratings (indicated by the line within each box) remain relatively stable over the years, hovering around the 7 to 8 range. This suggests a consistent level of content quality as perceived by viewers throughout the time period analyzed.

2. **Interquartile Range**: The interquartile range (IQR), represented by the height of each box, is fairly consistent, suggesting similar variability in ratings year over year. This implies that Netflix has maintained a stable content satisfaction level among its viewers.

3. **Outliers**: There are a few outliers each year, particularly on the lower end of the rating scale, indicating that while most content is well-received, there are always a few titles with significantly lower ratings.

4. **Slight Increase in Rating Variability**: In recent years, the 'whiskers' of the box plot, which indicate the range of the data excluding outliers, seem to extend slightly further than in earlier years, particularly the lower whisker. This could mean a broader diversity in content reception, with more titles having lower ratings.

5. **High-Rating Outliers**: There are occasional outliers on the high end of the rating scale, particularly in the earlier years, which suggests that there were some exceptionally well-received titles during those years.

6. **Overall Rating Quality**: The bulk of the content each year is rated between 6 and 9, which indicates a generally positive reception of Netflix content by its viewers.



Comparative Analysis of Netflix Ratings Across Different Genres

1. **Overall Rating Distribution**: The ratings for all genres are generally above average (above a 5 out of 10), which suggests a generally positive reception across all types of content.

2. **Consistency Across Genres**: Most genres show a median rating around 7 to 8, indicating a consistent level of viewer satisfaction across different types of content.

3. **Outliers Indicating Variation**: Several genres exhibit outliers, both on the lower and higher ends of the rating scale. Outliers on the upper end suggest the presence of exceptionally well-received content within those genres, whereas lower outliers might indicate a few titles that were not as well-received.

4. **Comparatively Lower Ratings in Certain Genres**: Some genres, such as 'Western' and 'Reality-TV', show a lower third quartile and median, which may point to these genres being less consistently popular among viewers.

5. **Genre-Specific Range**: The range (difference between the minimum and maximum non-outlier ratings) varies by genre. 'Biography' and 'Sport' show a relatively narrow interquartile range, suggesting a more consistent viewer rating pattern, whereas genres like 'Documentary' and 'Talk Show' exhibit a wider range, indicating more variability in how viewers rate these titles.

6. **Median Ratings Stability**: The median line within each box is positioned closer to the top of the box in most genres, suggesting that the ratings are skewed towards the higher end, and more than half of the content in each genre is rated above the median.




## Contributing
Contributions to this project are welcome. Please feel free to fork the repository and submit pull requests.

## License
[MIT License](LICENSE.md)

