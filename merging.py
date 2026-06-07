import pandas as pd

df = pd.read_csv('GeoLite2-Country-Locations-fr.csv', keep_default_na=False)

continents_data = {
    'continent_code': ['EU', 'AS', 'AF', 'NA', 'SA', 'OC', 'AN'],
    'continent_english': ['Europe', 'Asia', 'Africa', 'North America', 'South America', 'Oceania', 'Antarctica']
}
df_continents = pd.DataFrame(continents_data)

merged_df = pd.merge(df, df_continents, on='continent_code', how='left')

print("--- Successfully Merged Tables ---")
print(merged_df[['country_name', 'continent_code', 'continent_english']].head(10))