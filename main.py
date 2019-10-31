import pandas as pd

# Import marketing.csv
marketing = pd.read_csv('marketing.csv')

# Examining the data
print(marketing.head())

# Print the statistics of all columns
print(marketing.describe())

# Check column data types and non-missing values
print(marketing.info())