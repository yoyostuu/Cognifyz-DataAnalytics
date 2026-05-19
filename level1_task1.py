import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Dataset.csv", encoding='latin-1')
print(df.columns)
top_cuisines = df['Cuisines'].value_counts().head(3)#value count counts the number of times each cuisine appears in the dataset and head(3) gives the top 3 cuisines
print(top_cuisines)
total_restaurants = len(df)

percentage = (top_cuisines / total_restaurants) * 100

print(percentage)
top_cuisines.plot(kind='bar')

plt.title("Top 3 Most Common Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Number of Restaurants")

plt.show() 

# Insights:
# 1. North Indian cuisine appears most frequently.
# 2. The top cuisines dominate a large percentage of restaurants.
# 3. Customer preference trends can help business expansion decisions.