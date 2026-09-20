# Pandas --> Analyze the data
# Matplotlib --> show the data visually --> converts numbers to charts

# csv/database --> Pandas (Read, Clean, Analyze) --> Matplotlib (charts) --> Business Insights


# Module -14, 15, 20, 21

## Pandas I/O Demo
# Dataset = Table

# Excel, CSV, SQL DB, API, JSON, HTML, Parquet, Feather, HDF5, Msgpack, Stata, SAS, SPSS

import pandas as pd

# pd.read_<format>(path) ## load data from a file into a DataFrame

# df.to_<format>(path) ## write data from a DataFrame to a file

df = pd.read_csv("ecommerce_orders.csv")  # Load data from a CSV file into a DataFrame

print(df.shape)  # Print the shape of the DataFrame (number of rows and columns)
print(df.head())  # Print the first few rows of the DataFrame

df.head(10).to_csv("top_10_orders.csv", index=False)  # Save the first 10 rows of the DataFrame to a CSV file
