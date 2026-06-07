import pandas as pd

df = pd.read_csv('GeoLite2-Country-Locations-fr.csv', keep_default_na=False)

missing_continents = df[df['continent_code']== '']

print("Regions with Missing Continent Codes:")
print(missing_continents['continent_name'].unique())