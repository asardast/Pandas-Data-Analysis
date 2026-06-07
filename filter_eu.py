import pandas as pd

df = pd.read_csv('GeoLite2-Country-Locations-fr.csv')

eu_countries = df[df['is_in_european_union'] == 1]

print(eu_countries['country_name'])
