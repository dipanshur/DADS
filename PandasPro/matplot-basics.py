import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ecommerce_orders.csv")

df = df.drop_duplicates()

revenue_by_catagory = df.groupby("ProductCategory")["TotalAmount"].sum().sort_values(ascending=False)
orders_by_status = df["DeliveryStatus"].value_counts()
print(revenue_by_catagory)
print(orders_by_status)

plt.figure(figsize=(8, 5))

plt.bar(revenue_by_catagory.index, revenue_by_catagory.values, color="steelblue")

plt.title("Revenue by Product Catagory (PyPlot Interface)")
plt.xlabel("Product Catagory")
plt.ylabel("Total Revenue in Rs.")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("./01_pyplot_bar.png")
plt.close()

fig, ax = plt.subplots(figsize=(8,5)) ## fig = the whole canvas, ax = chart

ax.bar(revenue_by_catagory.index, revenue_by_catagory.values, color="steelblue")

ax.set_title("Revenue by Product Catagory (PyPlot Interface)")
ax.set_xlabel("Product Catagory")
ax.set_ylabel("Total Revenue in Rs.")
ax.tick_params(rotation=45, axis="x")
fig.tight_layout()
fig.savefig("./02_pyplot_bar.png")
plt.close(fig)

fig, axes = plt.subplots(2,2,figsize = (12,9))

axes[0,0].bar(revenue_by_catagory.index, revenue_by_catagory.values, color="teal")
axes[0,0].set_title("Revenue by Product Catagory")
axes[0,0].tick_params(axis="x", rotation=45)

axes[0,1].pie(orders_by_status.values, labels=orders_by_status.index)
axes[0,1].set_title("Deliver Status Breakdown")

axes[1,0].hist(df["TotalAmount"], bins=30, color="indianred")
axes[1,0].set_title("Distribution of Order Values")
axes[1,0].set_xlabel("Total Amountin Rs.")
axes[1,0].set_ylabel("Number of Orders")

axes[1,1].scatter(df["Quantity"], df["TotalAmount"], alpha=0.1, color="seagreen")
axes[1,1].set_title("Quantity VS Order value")
axes[1,1].set_xlabel("Quantity")
axes[1,1].set_ylabel("Total Amount in Rs.")


fig.suptitle("E-Commerce Orders - Overview Dashboard", fontsize=16)
fig.tight_layout()
fig.savefig("./03_ecom_dash.png")
plt.close(fig)
