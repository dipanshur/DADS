# Reshaping --> changing the layout of a DataFrame

# wide (one cols per category) --> long = melt()
# long (one row per observation) --> wide = pivot()


import pandas as pd

df = pd.read_csv("./ecommerce_orders.csv")

df = df.drop_duplicates()

df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["OrderMonth"] = df["OrderDate"].dt.to_period("M").astype(str)


# 1. Pivot Table -> long format to wide format

pivot_revenue = df.pivot_table(
    values ="TotalAmount",
    index = "OrderMonth",
    columns="ProductCategory",
    aggfunc="sum",
    fill_value=0
)

print("Pivoted Table - monthas row, categories as cols, revenues as value")
print(pivot_revenue.round(0).head(6))


# 2. melt() --> wide to long

pivot_reset = pivot_revenue.reset_index()

melted = pivot_reset.melt(
    id_vars= "OrderMonth",
    var_name="ProductCategory",
    value_name="Revenue"
)

print(f"melted back to long format")
print(melted.head(20))

