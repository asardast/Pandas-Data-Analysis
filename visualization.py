import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('GeoLite2-Country-Locations-fr.csv', keep_default_na=False)


continent_counts = df.groupby('continent_name').size().sort_values(ascending=True)

# (Bar Chart)
continent_counts.plot(kind='barh', color='skyblue', edgecolor='black')


plt.title('Number of Countries per Continent')
plt.xlabel('Number of Countries')
plt.ylabel('Continent')


plt.savefig('continent_chart.png', bbox_inches='tight')
print("--- Success! Chart saved as continent_chart.png ---")