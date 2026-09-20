## Correlation --> measures how strongly two numeric cols move together, +1 to -1, 0 means no correlation 
#              --> spot redunant features
#              --> multicollinearity


# unit price = 10rs --> 12
# quantity = 1
# Total amount = unit price

import pandas as pd
import numpy as np

df = pd.read_csv("ecommerce_orders.csv")
df = df.drop_duplicates()  # drop duplicates

numeric_cols = ["Quantity",	"UnitPrice", "Discount_pct", "ShippingCost", "TotalAmount"]

# TotalAmount = unitPrice x Quantity x disc + shipping

# .corr() --> computes the Pearson correlation coefficient between all numeric columns in the dataframe. The result is a correlation matrix that shows the pairwise correlation values between each pair of numeric columns.

# +1 = perfect positive correlation (as one variable increases, the other variable also increases)
# -1 = perfect negative correlation (as one variable increases, the other variable decreases)
# 0 = no correlation

corr_matrix = df[numeric_cols].corr()

print(corr_matrix.round(2))  # round to 2 decimal places

# 1. Find highly correlated pairs ( a simple threshold based check)

upper_triangle = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
print(upper_triangle.round(2))

threshold = 0.5
print(f"\nPair with correlation stronger than {threshold} (Positive or Negative):")
found_any = False

for col in upper_triangle.columns:
    for row in upper_triangle.index:
        value = upper_triangle.loc[row, col]
        if pd.notna(value) and abs(value) > threshold:
            print(f"  {row} <--> {col}: {value:.2f} ")
            found_any = True

if not found_any: 
    print("None found above this threshold")

# 2.
df_reduced = df.drop(columns=["TotalAmount"])

corr_matrix_reduced = df_reduced[[col for col in numeric_cols if col != "TotalAmount"]].corr()
print(corr_matrix.round(2))  # round to 2 decimal places
print(corr_matrix_reduced.round(2))  # round to 2 decimal places    

# 3. Correlation with a target column 

target_correlation = corr_matrix["TotalAmount"].sort_values(ascending=False)

print(f"\nCorrelation with Target Column 'TotalAmount':")
print(target_correlation.round(2))
