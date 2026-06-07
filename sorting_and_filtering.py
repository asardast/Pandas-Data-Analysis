import pandas as pd

df = pd.read_csv('GeoLite2-Country-Locations-fr.csv', keep_default_na=False)

non_eu_europe = df[(df['continent_code'] == 'EU') & (df['is_in_european_union'] == 0)]

sorted_countries = non_eu_europe.sort_values(by='country_name')

print(" European Countries NOT in the European Union (Sorted)")
print(sorted_countries['country_name'].to_string(index=False))