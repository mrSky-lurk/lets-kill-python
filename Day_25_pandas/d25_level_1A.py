import csv
import pandas as pd
from pathlib import Path

# Read the hacker_news.csv file from data directory
# Get the first five rows
# Get the last five rows
# Get the title column as pandas series
# Count the number of rows and columns
# Filter the titles which contain python
# Filter the titles which contain JavaScript
# Explore the data and make sense of it
# ================================================================================================================
def read_csv_file(file_name):
    csv_file_path = Path(__file__).resolve().parents[1] / "data" / file_name
    csv_df = pd.read_csv(csv_file_path)
    return csv_df

csv_df = read_csv_file("hacker_news.csv")
print("First 5 rows:: \n",csv_df.head())
print("last 5 rows:: \n",csv_df.tail())

print(csv_df.columns)
print(csv_df['title'][5])

print("Title column as pandas series - \n")
print(pd.Series(csv_df.columns))

print("Number of rows x columns:: ", csv_df.shape)

print("title which contains 'python'")
print(csv_df[csv_df['title'].str.contains('python', case=False, na=False)]['title'])

print("title which contains 'JavaScript'")
print(csv_df[csv_df['title'].str.contains('JavaScript', case=False, na=False)]['title'])



