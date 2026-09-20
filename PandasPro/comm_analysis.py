import pandas as pd

df = pd.read_csv("ecommerce_orders.csv")  # Load data from a CSV file into a DataFrame

# print(df.shape)  # Print the shape of the DataFrame (number of rows and columns)
# print(df.head())  # Print the first few rows of the DataFrame

# checks EVERY cell in the DataFrame for missing values and
# adds them up per column - this is the standard first check on any new dataset.

# print(df.isnull().sum())

# removes rows that are IDENTICAL across every single column.

# print(df.duplicated().sum())

# df = df.drop_duplicates()

# print(df.duplicated().sum())

# print(df[df["CustomerID"] == "CUST0122"])

# df["CustomerName"] = df["CustomerName"].fillna("Unknown Customer")

# print(df[df["CustomerID"] == "CUST0122"])

# Q - Overall business snapshot --> sum and mean

total_orders = len(df)
total_revenue = df["TotalAmount"].sum()
average_order_value = df["TotalAmount"].mean()

print(total_orders, total_revenue, round(average_order_value, 2))

# Q - Revenue by Catagory

revenue_by_category = df.groupby("ProductCategory")["TotalAmount"].agg(["sum", "mean", "count"])

print(revenue_by_category)

# Q - Orders per City

orders_by_city = df["City"].value_counts() # unique cities and their order counts
print(orders_by_city)

# Q - Payment Method Preference - 

payment_count = df["PaymentMode"].value_counts()
print(payment_count)

# Q - Cancellation rate no of cancelled order/total orders * 100

cancelled_orders = (df["DeliveryStatus"] == "Cancelled").sum()

cancel_rate = (cancelled_orders/total_orders) * 100

print(cancel_rate)

# Q - Top Costomer by Spending

spending_by_customer = df.groupby("CustomerName")["TotalAmount"].sum()
spending_by_customer = spending_by_customer.sort_values(ascending=False)
print(spending_by_customer.head(1))

# Q - Best-selling products by units, not revenue - groupby + sum() on Quantity.

unitsold = df.groupby("ProductName")["Quantity"].sum()
unitsold = unitsold.sort_values(ascending=False)
print(unitsold.head(5))