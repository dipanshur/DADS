import pandas as pd

df = pd.read_csv("data_csv.csv", usecols=["name", "city"], nrows=2)


# df = pd.read_csv("data_csv.csv", sep=";")

print(df)

df.to_csv("output.csv", index=True)
