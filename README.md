# GeoLite2 Data Analysis Project with Pandas

This project explores and analyzes country location data from the MaxMind GeoLite2 database using **Python** and **Pandas**. It is structured as a practical portfolio for data manipulation, cleaning, and visualization.

## 📁 Project Structure

* `GeoLite2-Country-Locations-fr.csv`: The source dataset containing global country records in French.
* `filter_eu.py`: Filters and displays countries belonging to the European Union.
* `continent_stats.py`: Performs data aggregation to count countries per continent.
* `clean_data.py`: Handles missing values and fixes the famous `NA` (North America) string interpretation bug in Pandas.
* `sorting_and_filtering.py`: Advanced multi-conditional filtering and alphabetical sorting.
* `updating_data.py`: Data transformation by mapping French continent names to English in a new column.
* `export_outputs.py`: Exports processed data into production-ready **Excel (.xlsx)** and **JSON** formats.
* `visualization.py`: Generates a horizontal bar chart of country distributions.

## 🛠️ How to Run

1. Clone this repository.
2. Activate your virtual environment and install dependencies:
   ```bash
   pip install pandas openpyxl matplotlib
