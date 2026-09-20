# person 1 - 20 years - 170
# person 2 - 20 years - 180

# height -- cm (150-200)
# Age -- years (1-100)

# every column and reshape its number => average of aolumn = 0, spread = 1
# new_value = (original value - column average) /column spread

# scaled_value = (original_value - column_mean) / column_std

# average + spread ==> training data --> test data

# # make the numbers fair to compare

# mean and standard deviation

# 2 4 6 8 10 12

import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("./ecommerce_orders.csv")
df = df.drop_duplicates()

numeric_cols = ["Quantity",	"UnitPrice", "Discount_pct", "ShippingCost", "TotalAmount"]

X = df[numeric_cols].copy()

print(X.describe().loc[["mean", "std", "min", "max"]].round(2))

#step1 --> create a scaler object
scaler = StandardScaler()

# step2 --> fit (cal mean and std of each col) + transform (applied (value - mean) / std)
X_scaled = scaler.fit_transform(X)

X_scaled_df = pd.DataFrame(X_scaled, columns=numeric_cols, index=X.index)

print("After Scaling- every col now has mean approx 0 and std approx 1: ")
print(X_scaled_df.describe().loc[["mean", "std", "min", "max"]].round(2))

print("\nFirst 5 rows before scaling: ")
print(X.head())

print("\nFirst 5 rows after scaling: ")
print(X_scaled_df.head().round(2))

print(dict(zip(numeric_cols, scaler.mean_.round(2))))
print(dict(zip(numeric_cols, scaler.scale_.round(2))))

# store the exact number it learned per col


# st1 = 5/10(50%) value edu + 60/100(60%) sci = 50+60/2 =55% = 0.55 

# algorithm --> Judge col by their predictive value noy by raw value --> same footing

# 1. sanity check --> -1 to +1 ++ ==> 6.44 (usually large number + Above average)
# Neural networks
# PCA --> Principal Component Analysis --> 
# Liniar/logistics regression


# 12 13 asdkjfhakshd 12312 342 1234 325324 5234 523 4523 45 23452 34

# 1 2 3 4 5 6 7 8 9 