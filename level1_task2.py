# City Analysis - Cognifyz Data Analytics Internship
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Dataset.csv", encoding='latin-1')
print(df.head())
print(df.columns)
print(df.info())
print(df.shape)
city_counts = df['City'].value_counts()
print(city_counts.head())
avg_rating = df.groupby('City')['Aggregate rating'].mean()
print(avg_rating.sort_values(ascending=False).head()) 
city_counts.head(10).plot(kind='bar')
#top 10 cities by number of restaurants graph
plt.title("Top Cities by Number of Restaurants")
plt.xlabel("City")
plt.ylabel("Restaurant Count")
plt.show()
#top 10 cities by average rating graph
avg_rating.sort_values(ascending=False).head(10).plot(kind='bar')
plt.title("Top Cities by Average Rating")
plt.xlabel("City")
plt.ylabel("Average Rating")

plt.show()
# Insights:
#1. New Delhi has the highest number of restaurants.
# 2. Some cities have significantly higher average ratings.
# 3. Restaurant distribution varies heavily across cities.