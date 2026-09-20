import pandas as pd

data = {
    "Departments": ["IT", "IT", "HR", "HR"],
    "Salary": [5000, 6000, 4500, 5500]

}

df = pd.DataFrame(data)

print(df)

print(df.groupby("Departments")["Salary"].agg(["mean", "max", "min", "sum"]))