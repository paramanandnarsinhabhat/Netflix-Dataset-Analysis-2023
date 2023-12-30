
# Netflix Dataset Analysis 

## Project Overview
This project focuses on analyzing the Netflix dataset for the year 2010 to 2023. The analysis covers various aspects such as viewership trends, ratings, and content preferences globally. The goal is to derive meaningful insights that can help understand viewer behavior and preferences.

## Data Source
The dataset used in this project is titled `total_netflix_2023.csv` and includes information on various Netflix titles, their release dates, viewership hours, ratings, and other relevant details.

## Repository Structure
Netflix-Dataset-Analysis-2023/

│
├── data/
│   ├── processed/
│   │   └── netflix_data_cleaned.csv
│   └── raw/
│       └── total_netflix_2023 new.csv
│
├── myenv/
│   ├── bin/
│   ├── include/
│   ├── lib/
│   └── pyvenv.cfg
│
├── notebooks/
│   └── Netflix_notebook.ipynb
│
├── scripts/
│   ├── __init__.py
│   ├── data_cleaning.py
│   ├── data_loading.py
│   ├── data_visualization_bar_chart.py
│   ├── data_visualization_box_plot.py
│   ├── data_visualization_genreratings.py
│   ├── data_visualization_heatmap.py
│   ├── data_visualization_scatterplotsratingvsviewer.py
│   └── data_visualization_stacked_bar_chart.py
│
├── utils/
│   ├── __init__.py
│   └── data_utils.py
│
├── .gitignore
├── README.md
└── requirements.txt



# Project File Structure

This section outlines the organization of the project repository and provides a description for each component.

## data
Contains raw and processed datasets.

- `/raw`: Includes the original dataset files as they were obtained.
  - `total_netflix_2023 new.csv`: Original dataset with Netflix titles for the year 2023.

- `/processed`: Contains datasets that have been cleaned and processed.
  - `netflix_data_cleaned.csv`: Cleaned version of the Netflix dataset, ready for analysis.

## myenv
Python virtual environment folder containing all the necessary packages and their versions.

## notebooks
Jupyter notebooks with detailed code, output, and explanations for analysis and visualization.

- `Netflix_notebook.ipynb`: Jupyter notebook containing the exploratory data analysis and visualization code.

## scripts
Python scripts for data processing and visualization.

- `data_cleaning.py`: Script for cleaning the dataset.
- `data_loading.py`: Script for loading the dataset.
- `data_visualization_bar_chart.py`: Script for creating bar chart visualizations.
- `data_visualization_box_Plot.py`: Script for creating box plot visualizations.
- `data_visualization_genreratings.py`: Script for generating genre ratings visualizations.
- `data_visualization_heatmap.py`: Script for creating heatmap visualizations.
- `data_visualization_scatterplotsratingvsviewer...`: Script for creating scatter plots of ratings vs. viewership hours.
- `data_visualization_stacked_bar_chart.py`: Script for creating stacked bar chart visualizations.
- `data_visualization_viewershiphours.py`: Script for creating viewership hours visualizations.

## utils
Utility functions used across the project.

- `data_utils.py`: Contains utility functions for data loading, cleaning, and saving.

## Root Directory Files

- `.gitignore`: Specifies intentionally untracked files to ignore by Git.
- `readme.md`: Markdown file with a detailed description of the project, its structure, setup instructions, and usage.
- `requirements.txt`: Contains a list of items to be installed using `pip install -r requirements.txt`.


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


Temporal Dynamics of Netflix Content Release: A Monthly and Yearly Perspective

1. **Content Release Growth**: The heatmap shows a clear trend of increasing content releases over the years. Starting with sparse activity in the early 2010s, there is a noticeable ramp-up in the volume of titles released as the years progress.

2. **Seasonal Patterns**: There appears to be seasonality in content release, with certain months, like October and December, consistently having higher numbers of releases. This could be due to strategic planning around holiday seasons or periods of higher viewer engagement.

3. **Recent Years Saturation**: The most saturated colors, indicating the highest number of releases, appear in the later years across several months, suggesting a strategy shift towards more frequent content updates.

4. **Pandemic Era Content Boost**: The years 2020 and 2021 show particularly high numbers of releases across almost all months, which could be associated with the increased demand for streaming content during the COVID-19 pandemic when people spent more time at home.

5. **Notable Peaks**: The heatmap highlights specific months with exceptionally high release volumes, such as March and October of 2022, which could be points of interest for further investigation into the cause of these peaks.

6. **Data Collection Timeframe**: The year 2023 shows data only up to a certain point, likely indicating that the data for the rest of the year has not been collected or that the year is ongoing.



Dissecting the Relationship Between Ratings and Viewership on Netflix


1. **Wide Range of Viewership**: The viewership hours vary widely across the dataset, ranging from titles with very few hours to those with viewership in the tens of millions. This indicates a significant disparity in how much certain titles are watched compared to others.

2. **Rating Distribution**: Most of the data points cluster in the range of 6 to 8 on the rating scale, suggesting that the majority of titles have ratings that fall within this range, which is typically considered above average.

3. **No Clear Correlation**: At first glance, there does not appear to be a strong linear correlation between ratings and viewership hours. High viewership hours can be observed across a range of ratings, not exclusively associated with the highest ratings.

4. **Presence of Outliers**: There are outliers in viewership hours, particularly a few titles with exceptionally high hours viewed that do not necessarily have the highest ratings. This could indicate that factors other than ratings can drive viewership, such as marketing, timing of release, or social phenomena.

5. **Dense Concentration at Lower Viewership**: A dense concentration of data points at the lower end of viewership hours suggests that a large number of titles have relatively low viewership, which is common in content distribution platforms.

6. **High Ratings Without High Viewership**: There are titles with high ratings (close to 10) that do not correspond to the highest viewership hours, implying that a high rating does not guarantee a high viewership.

Evolving Trends in Genre Popularity on Netflix from 2010 to 2023

1. **Overall Growth**: There is a clear upward trend in the total number of titles across all genres, indicating Netflix's expanding content library over the years.

2. **Dominant Genres**: Drama and Comedy appear to be consistently dominant genres throughout the years, often taking up the largest proportions of the content stack. This could reflect a steady demand for these genres among Netflix's audience.

3. **Emerging Genres**: Animation and Documentary genres show growth over time, suggesting a strategic diversification of Netflix's content offerings to cater to a wider range of viewer preferences.

4. **Variability in Genre Popularity**: Some genres, such as Horror and Biography, maintain a relatively small proportion of the content stack each year, which could indicate a niche but stable audience for these genres.

5. **Shift in Focus**: The later years, particularly 2021-2022, show a significant increase in Documentary and Adventure titles, possibly reflecting a shift in Netflix’s content strategy or responding to changing viewer interests.

6. **Decrease in 2023**: There's a noticeable decrease in the number of titles in 2023 across all genres. This might be due to incomplete data for the year if it's still ongoing, or it could signify a shift in Netflix's content acquisition or production strategy.

7. **Content Saturation and Strategy Adjustment**: The sharp increase in content volume in the years leading up to 2023, followed by a drop, could suggest a period of content saturation and subsequent strategy adjustment by Netflix.



Disparities in Genre Watch-Time: An In-Depth Look at Netflix Viewership Hours


1. **High Variance in Viewership**: There is a substantial variance in viewership hours across different genres, with some genres showing a significantly wider range of hours watched. This suggests that certain genres may have a few standout titles with exceptionally high viewership that drive up the total hours.

2. **Popular Genres**: Some genres, such as 'Drama' and 'Comedy', have numerous data points spread across a range of viewership hours, indicating a broad appeal and consistent production of content in these categories.

3. **Outliers Indicating Blockbusters**: There are notable outliers in genres like 'Action' and 'Adventure', which may correspond to blockbuster titles with high viewership. Such outliers could significantly influence the average viewership hours for their respective genres.

4. **Lower Average Viewership in Niche Genres**: Genres such as 'Documentary', 'Musical', and 'Western' appear to have fewer titles with high viewership hours, which could indicate a more niche audience or less frequent production of high-impact titles in these categories.

5. **Consistency Among Certain Genres**: Genres such as 'Crime' and 'Horror' show a consistent cluster of viewership hours, suggesting a steady audience engagement without extreme peaks in viewership.

6. **Potential for Audience Expansion**: The genres with lower viewership hours present an opportunity for Netflix to expand its audience by investing in content that can attract more viewers or by promoting existing content to wider audiences.

7. **Strategic Content Placement**: The distribution of viewership hours by genre could inform Netflix's content strategy, highlighting which genres might benefit from further investment and development.


## Contributing
Contributions to this project are welcome. Please feel free to fork the repository and submit pull requests.

## License
[MIT License](LICENSE.md)

