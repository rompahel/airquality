import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page configuration
st.set_page_config(page_title="Air Quality Analysis Dashboard", layout="wide")

# Title and Introduction
st.title('Proyek Analisis Data: Air Quality Dataset Aotizhongxin')
st.markdown('**Nama:** Ronald Silvester Sanger')
st.markdown('**Email:** m180b4ky3964@bangkit.academy')
st.markdown('**ID Dicoding:** ronald_silvester')

# Questions
st.header('Pertanyaan Bisnis')
st.markdown('1. What is the correlation between wind speed (WSPM) and PM2.5 concentration levels?')
st.markdown('2. Are there identifiable seasonal patterns in PM10 concentration levels across different months or seasons?')

# Import Libraries Section
st.header('Import Semua Packages/Library yang Digunakan')
st.code("""
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
""", language='python')

# Data Wrangling and Loading Data
st.header('Data Wrangling')
st.subheader('Gathering Data')
url = 'https://raw.githubusercontent.com/rompahel/airquality/refs/heads/main/data/Cleaned_PRSA_Data_20130301-20170228(2).csv'

# Load the dataset
data = pd.read_csv(url)
st.dataframe(data.head())

# Data Assessment Insight
st.markdown('**Insight:** The dataset shows data of air quality metrics such as PM2.5, PM10, SO2, NO2, CO, and O3, including meteorological data like temperature (TEMP), wind speed (WSPM), and pressure (PRES), enabling the analysis of environmental factors that influence air quality.')

# Data Visualization - Scatter Plot of PM2.5 vs. Wind Speed (WSPM)
st.header('Exploratory Data Analysis (EDA)')
st.subheader('Scatter Plot of PM2.5 vs. Wind Speed (WSPM)')

# Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='WSPM', y='PM2.5', data=data, alpha=0.5)
plt.title('Scatter Plot of PM2.5 vs Wind Speed (WSPM)')
plt.xlabel('Wind Speed (WSPM)')
plt.ylabel('PM2.5 Concentration')
plt.grid(True)
st.pyplot(plt)

# Insight for Scatter Plot
st.markdown("""
**Insight:**
- The correlation coefficient between wind speed (WSPM) and PM2.5 concentration is approximately -0.28, indicating a weak negative correlation.
- This means that, as wind speed increases, PM2.5 concentration tends to slightly decrease.
- The scatter plot visualizes this relationship, showing that there is some tendency for higher wind speeds to be associated with lower PM2.5 levels, though the trend is not very strong.
""")

# Seasonal Average PM10 Concentration Bar Chart
st.subheader('Average PM10 Concentration Levels by Season')

# Bar Chart
seasonal_pm10 = data.groupby('season')['PM10'].mean().reindex(['Winter', 'Spring', 'Summer', 'Fall'])
plt.figure(figsize=(8, 6))
seasonal_pm10.plot(kind='bar', color='skyblue')
plt.title('Average PM10 Concentration Levels by Season')
plt.xlabel('Season')
plt.ylabel('Average PM10 Concentration')
plt.xticks(rotation=0)
st.pyplot(plt)

# Insight for Bar Plot
st.markdown("""
**Insight:**
- The average PM10 concentration levels by season are:
  - **Winter:** 116.98
  - **Spring:** 132.04
  - **Summer:** 81.51
  - **Fall:** 110.09
- The bar plot shows that Spring has the highest average PM10 concentration, while Summer has the lowest.
- This indicates a potential seasonal pattern where air quality improves during the summer and worsens in the spring.
""")

# Correlation Heatmap Visualization
st.subheader('Correlation Analysis')

# Correlation heatmap of meteorological variables
plt.figure(figsize=(10, 8))
correlation_matrix = data[['WSPM', 'PM2.5', 'PM10', 'TEMP', 'PRES', 'DEWP', 'RAIN']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of Meteorological Variables')
st.pyplot(plt)

# Insight for Heatmap
st.markdown("""
**Insight:**
- The heatmap reveals a weak negative correlation between wind speed (WSPM) and PM2.5 levels, indicating that higher wind speeds tend to slightly reduce the concentration of PM2.5 particles in the air.
- This supports the idea that wind plays a role in dispersing particulate matter, contributing to better air quality.
""")

# Monthly Average PM10 Levels Over Time
st.subheader('Seasonal Trends in PM10 Levels')
data['year_month'] = data['year'].astype(str) + '-' + data['month'].astype(str).str.zfill(2)
monthly_pm10 = data.groupby('year_month')['PM10'].mean()

# Plotting the monthly trend
plt.figure(figsize=(12, 6))
monthly_pm10.plot(kind='line', marker='o')
plt.title('Monthly Average PM10 Levels Over Time')
plt.xlabel('Year-Month')
plt.ylabel('Average PM10 Levels')
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)

# Insight for Monthly Trend
st.markdown("""
**Insight:**
- The line plot of monthly average PM10 levels shows clear seasonal variations, with higher concentrations observed in Spring and lower levels during the Summer.
- This trend suggests that air quality tends to worsen in Spring, possibly due to increased industrial activity or natural events, and improves in Summer, likely due to favorable weather conditions.
""")

# Conclusions Section
st.header('Kesimpulan')
st.markdown("""
**Conclusion:**

- **Correlation between Wind Speed (WSPM) and PM2.5 Levels:**
  - The correlation coefficient between WSPM and PM2.5 is approximately -0.28, indicating a weak negative correlation.
  - This suggests that higher wind speeds tend to slightly reduce the concentration of PM2.5 particles in the air.
  - Although the correlation is not very strong, it implies that wind can help disperse particulate matter, contributing to better air quality.

- **Seasonal Patterns in PM10 Concentration Levels:**
  - The seasonal analysis reveals distinct patterns in PM10 levels. Spring has the highest average concentration of PM10 (132.04), while Summer has the lowest (81.51).
  - This pattern suggests that air quality tends to worsen in Spring and improve in Summer, likely due to a combination of seasonal factors such as increased industrial activity, weather patterns, and natural events like dust storms.
""")
