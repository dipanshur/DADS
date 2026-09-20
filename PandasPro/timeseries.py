## Time series --> time matters --> revenue by day. temprature by hour. stock price by minute.

import pandas as pd

df = pd.read_csv("./ecommerce_orders.csv")
df = df.drop_duplicates()

# 1.convert datetime and set it as index.

df["OrderDate"] = pd.to_datetime(df["OrderDate"], dayfirst=True)
df = df.sort_values("OrderDate")    
ts = df.set_index("OrderDate")["TotalAmount"] ## a series of revenvue , indexed by date.

print(ts.head())
print(f"Date Range: ", ts.index.min(), "to", ts.index.max())


# 2. Extract Date parts ()

df["Year"] = df["OrderDate"].dt.year
df["Month"] = df["OrderDate"].dt.month
df["Weekday"] = df["OrderDate"].dt.day_name()
df["Quarter"] = df["OrderDate"].dt.quarter

print(f"Order Per year")
print(df["Year"].value_counts().sort_index())

# 3. Resampling - Group by time period

montly_revenue = ts.resample("ME").sum()
print(f"Monthly revenue (first 6 Months)")
print(montly_revenue.head(6).round(2))

monthly_order_count = ts.resample("ME").count()
print(f"Monthly Order Count (first 6 Months)")
print(monthly_order_count.head(6))

# 4. Rolling Window -- Smooth out the short term noise

rolling_3month_avg = montly_revenue.rolling(window=3).mean()
print(f"Monthly reveneu vs its 3 months rolling average")
comparision = pd.DataFrame({
    "Monthly Revenue": montly_revenue,
    "3 Months Rolling average": rolling_3month_avg
}).round(2)

print(comparision.head(6))

# 5. Shift --> compare current month revenue with previous month revenue

monthly_df = montly_revenue.to_frame(name="Revenue")
monthly_df["Previous Month Revenue"] = monthly_df["Revenue"].shift(1)
monthly_df["Month_Over_Month_change_pct"] = (
    (monthly_df["Revenue"] - monthly_df["Previous Month Revenue"])/monthly_df["Previous Month Revenue"] * 100
).round(1)

print("Month-over-Month Revenue change")
print(monthly_df.head(6))