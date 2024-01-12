import pandas as pd

# Read the CSV file
df = pd.read_csv('data/winemag-data-130k-v2.csv.zip', compression='zip')

# Group by country and calculate the required statistics
summary_data = df.groupby('country').agg({
    'points': 'mean',
    'title': 'count'
}).reset_index()

# Rename columns for clarity
summary_data.columns = ['country', 'average_points', 'number_of_reviews']

# Write the summary data to a new CSV file
summary_data.to_csv('data/reviews-per-country.csv', index=False)

print("Summary data written to reviews-per-country.csv")# add your code here

