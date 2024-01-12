import pandas as pd

df = pd.read_csv('data/winemag-data-130k-v2.csv.zip', compression='zip')

summary_data = df.groupby('country').agg({
    'points': 'mean',
    'title': 'count'
}).reset_index()

summary_data.columns = ['country', 'average_points', 'number_of_reviews']
summary_data.to_csv('data/reviews-per-country.csv', index=False)

print("Summary data written to reviews-per-country.csv")

