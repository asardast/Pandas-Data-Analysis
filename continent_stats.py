import pandas as pd

df = pd.read_csv('GeoLite2-Country-Locations-fr.csv')

countries_per_continent = df.groupby('continent_name').size().sort_values(ascending=False)


print("Number of countries sort by continent:")
print(countries_per_continent)