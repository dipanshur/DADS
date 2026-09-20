import pandas as pd
import numpy as np
from math import sqrt
from sklearn.preprocessing import StandardScaler
from scipy import stats

# Load the dataset
df = pd.read_csv('data_science_master_course_dataset.csv')

print(df.shape) 

# (2525, 45)
# 2525 Observations and 45 Features/Variables

total_spend_12m_mean = df['total_spend_12m'].mean()
print(total_spend_12m_mean)

total_spend_12m_median = df['total_spend_12m'].median()
print(total_spend_12m_median)

total_spend_12m_max = df['total_spend_12m'].max()
print(total_spend_12m_max)

# print(df.dtypes)

print(df.head())
print(df.columns.to_list())
df.info()

missing = (df.isnull().sum().sort_values(ascending=False))

print(missing.head(10))

print(df.duplicated().sum())

df_clean = df.drop_duplicates()
print(df_clean.shape)

print(df[(df["customer_age"] < 18) | (df["customer_age"] > 100)][["customer_id", "customer_age"]])

print(df[["total_spend_12m", "annual_income", "previous_orders", "satisfaction_score"]].describe())

variance = df["total_spend_12m"].var()
print(variance)

std_variance = df["total_spend_12m"].std()
print(std_variance) ## 

## Euclidean distance between two points in a 2D space
distance = sqrt(
    (34-30) ** 2 + (13-10) ** 2
)

print(distance) ## 5.0

customer_a = df.iloc[0]
print(customer_a)
customer_b = df.iloc[1]

print(
    customer_a[
      [
          "customer_id",
          "customer_age",
          "previous_orders",
      ]
    ]
)

print(
    customer_b[
      [
          "customer_id",
          "customer_age",
          "previous_orders",
      ]
    ]
)

distance_customers = sqrt(
    (customer_a["customer_age"] - customer_b["customer_age"]) ** 2 +
    (customer_a["previous_orders"] - customer_b["previous_orders"]) ** 2
)
print(distance_customers)

featues = df[["customer_age", "previous_orders", "total_spend_12m"]].copy()

featues = featues.dropna()
scaler = StandardScaler()
scaled_features = scaler.fit_transform(featues)

sample = df.sample(n=500, random_state=42)
print(sample.shape)

print(df["total_spend_12m"].mean()) # Parameter of the population

# one sample t-test --> sample mean = population mean
# Independent t-test --> sample mean 1 = sample mean 2
# Paired t-test --> sample mean 1 = sample mean 2 (same sample, different time)
#Parametric Testing Assumptions: 
# 1. Numerical Data
# 2. Independent Observations
# 3. Appximate Normality
# 4. Homogeneity of Variance

print(sample["total_spend_12m"].mean())  # Statistic of the sample # Hypothesis testing --> sample mean = population mean

# H0 = Null Hypothesis: Sample mean = Population mean
# H1 = Alternative Hypothesis: Sample mean != Population mean

#Significance Level (alpha) = 0.05 = 5%
# p<0.05 --> reject H0
# p>=0.05 --> fail to reject H0

# Independent T-test --> sample mean 1 = sample mean 2

df["city_clean"] = (df["city"].str.strip().str.title())

pune = df.loc[df["city_clean"] == "Pune", "total_spend_12m"].dropna()
mumbai = df.loc[df["city_clean"] == "Mumbai", "total_spend_12m"].dropna()

print("Pune Mean:", pune.mean())
print("Mumbai Mean:", mumbai.mean())

#Welch's t-test --> does not assume equal variance between the two groups

t_stat, p_value = stats.ttest_ind(pune, mumbai, equal_var=False)
print("T-statistic:", t_stat)
print("P-value:", p_value)

## p = 0.71 > 0.05 --> fail to reject H0 --> Sample mean Pune = Sample mean Mumbai

# Based on this dataset, we do not have enough evidence to conclude that the average total annual spending differs between Pune and Mumbai customers

# Mathematically: Pune Mean != Mumbai Mean
# Statistically: Difference which may simply be due to random chance and sampling variability

# H0: ALL membership group hae the same mean spending
# H1: At least one membership group has a different mean spending

df["membership_tier_clean"] = (df["membership_tier"].str.strip().str.title())

bronze = df.loc[df["membership_tier_clean"] == "Bronze", "total_spend_12m"].dropna()
silver = df.loc[df["membership_tier_clean"] == "Silver", "total_spend_12m"].dropna()
gold = df.loc[df["membership_tier_clean"] == "Gold", "total_spend_12m"].dropna()
platinum = df.loc[df["membership_tier_clean"] == "Platinum", "total_spend_12m"].dropna()

f_stat, p_value = stats.f_oneway(bronze, silver, gold, platinum)
print("F-statistic:", f_stat)
print("P-value:", p_value)
#p<<0.05 --> reject H0 --> At least one membership group has a different mean spending

# Bronze = 9249
# silver = 32261
# Gold = 59588
# platinum = 220599

# 1. Parametric test - t-test, ANOVA, Paired t-test

# 2. Non-parametric test - mann - whitney test, wilcoxon test, kruskal wallis test, friedman test

# --> Confidence Coefficient

# Average spending = Rs 116449 ??
# range = confidence interval 

# 90%, 95%, 99% confidence interval, 95% = 0.95

spend = (df["total_spend_12m"].dropna())

n = len(spend)
spend_mean = spend.mean()
std_error = stats.sem(spend) # Standard Error of the Mean
print("standard error of the mean: ", std_error)


confidence_interval = stats.t.interval(0.95, n-1, loc=spend_mean, scale=std_error)

print("Mean: ", spend_mean)
print("Confidence Interval: ", confidence_interval)

# H0: mean = Rs 90000

# 95% confidence interval = (Rs 110,000, Rs 122,000)

# H0 = Null hypothesis
# H1 = Alternative hypothesis

# p < 0.05 --> reject H0
# p >= 0.05 --> fail to reject H0