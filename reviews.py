import pandas as pd
import numpy as np

data = pd.read_csv('data/winemag-data-130k-v2.csv')
print(data.head())
print(data.columns)
mean_points = data.groupby("country")["points"].mean().round(1)
data.country.value_counts()
value_counts = data.country.value_counts(ascending=False)
result = pd.concat([value_counts, mean_points], axis=1, join="inner")

print(result)
