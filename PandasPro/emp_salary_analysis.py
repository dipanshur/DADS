import pandas as pd

df = pd.read_csv("employee_salaries.csv")

# print(df.shape)
# print(df.isnull().sum())

desc = df["AnnualSalary"].describe().astype(float) 

# print(desc.map(lambda x: f"{x:,.2f}"))


# print(df["Education"].describe())

## Clean

df["Education"] = df["Education"].fillna("Not Specified")

# print(df.isnull().sum())

## Outlier Detection -->> IQR --> Interquartile Range


outlier_ids = []

for level in sorted(df["JobLevel"].unique()):
    level_data = df[df["JobLevel"] == level]

    q1 = level_data["AnnualSalary"].quantile(0.25)
    q3 = level_data["AnnualSalary"].quantile(0.75)

    iqr = q3 - q1

    lower_limit = q1 - 1.5*iqr
    upper_limit = q3 + 1.5*iqr

    too_low = level_data[level_data["AnnualSalary"] < lower_limit]
    too_high = level_data[level_data["AnnualSalary"] > upper_limit]

    outlier_ids.extend(too_low["EmployeeID"].tolist())
    outlier_ids.extend(too_high["EmployeeID"].tolist())

outliers = df[df["EmployeeID"].isin(outlier_ids)]
# print(outliers[["EmployeeID", "Name", "Department", "JobLevel", "AnnualSalary"]])

df_clean = df[~df["EmployeeID"].isin(outlier_ids)].copy()
# print(len(df_clean))




## Q1 --> the value at 25th percentile, Q3 --> the value at 75th percentile
## IQR --> Q3 - Q1 --> ranege covering  middle 50 %


# Q1 - 1.5*IQR => anything below this is outlier
# Q3 + 1.5*IQR => Anything above this is outlier


# 100 .. 75 .. 50 .. 25 ..  1


# Q1 - Company wide average vs median salary

avarage_salary = df["AnnualSalary"].mean()
median_salary = df["AnnualSalary"].median()

print(round(avarage_salary, 0), round(median_salary, 0))


##Q2 - Avarage salary by department
salary_by_dept = df_clean.groupby("Department")["AnnualSalary"].mean()
salary_by_dept = salary_by_dept.sort_values(ascending=False)
print(salary_by_dept.round(0))

# print(df.isnull().sum())

##Q3 --> Gendar pay comparision within each job level

salary_by_level_gender = df_clean.groupby(["JobLevel", "Gender"])["AnnualSalary"].mean()
print(salary_by_level_gender.round(0))

##Q4 --> Does Experience pridict Salary? --> Corr()

correlation = df_clean["Experience_Years"].corr(df_clean["AnnualSalary"])
print(round(correlation, 2))

# Q5 --> Does higher performance rating comes with higher average bonus?

bonus_by_rating = df_clean.groupby(["JobLevel", "PerformanceRating"])["Bonus"].mean()
print(bonus_by_rating.round(0))