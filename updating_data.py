import pandas as pd

df = pd.read_csv('GeoLite2-Country-Locations-fr.csv', keep_default_na=False)

# Creating a dictionary to translate continent names from French to English
continent_translation = {
    'Europe': 'Europe',
    'Asie': 'Asia',
    'Afrique': 'Africa',
    'Amérique du Nord': 'North America',
    'Amérique du Sud': 'South America',
    'Océanie': 'Oceania',
    'Antarctique': 'Antarctica'
}

# Creating a new column called 'continent_name_en' using the map function
df['continent_name_en'] = df['continent_name'].map(continent_translation)

print("Added New English Continent Column (Preview)")
print(df[['continent_name', 'continent_name_en', 'country_name']].head(10))