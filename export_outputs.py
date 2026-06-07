import pandas as pd

df = pd.read_csv('GeoLite2-Country-Locations-fr.csv', keep_default_na=False)

eu_only = df[df['is_in_european_union'] == 1]

# 1. Export as an Excel file
eu_only.to_excel('european_union_countries.xlsx', index=False)

# 2. Export as JSON file
eu_only.to_json('european_union_countries.json', orient='records', indent=4)

print("--- Success! Outputs exported as Excel and JSON files ---")