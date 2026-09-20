import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ecommerce_orders.csv")
df = df.drop_duplicates()

sns.set_style("whitegrid")

# 1. Categorical Plots --> countplot --> how many rows falls into each catagory, barplots --> shows the average of a numeric column per category

# Count Plot
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="ProductCategory", order=df["ProductCategory"].value_counts().index)
plt.title("Number of orders per ProductCategory")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("./05_countplot.png")

plt.close()

#Bor Plot
plt.figure(figsize=(8,5))
sns.barplot(data=df, x="ProductCategory", y="TotalAmount", order=df.groupby("ProductCategory")["TotalAmount"].mean().sort_values(ascending=False).index)
plt.title("Average Order Value per Product Category")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("./06_barplot.png")

plt.close()

# Box Plot
plt.figure(figsize=(8,5))
sns.barplot(data=df, x="ProductCategory", y="TotalAmount")
plt.title("Order value spread per Product Category")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("./07_boxplot.png")

plt.close()

#violin plot
plt.figure(figsize=(8,5))
sns.violinplot(data=df, x="DeliveryStatus", y="TotalAmount")
plt.title("Order value Distribution by delibery status")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("./08_violinplot.png")

plt.close()


# 2. Distribution plots --> histplot, kdeplot, displot

plt.figure(figsize=(8,5))
sns.histplot(data=df, x="TotalAmount", bins=30, kde=True, color="steelblue")
plt.title("Distribution of order values")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("./09_histplot.png")

plt.close()

#kde plot

plt.figure(figsize=(8,5))
sns.kdeplot(data=df, x="TotalAmount", hue="DeliveryStatus", fill=True, alpha=0)
plt.title("Order values Density by Delivery status")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("./10_kdeplot.png")

plt.close()

# Displot --> A figure level function, col= automatically create a small histogram per category

top_categories = df["ProductCategory"].value_counts().head(3).index
g = sns.displot(data=df[df["ProductCategory"].isin(top_categories)], x="TotalAmount", col="ProductCategory", bins=20, height=4)

g.savefig("./11_displot.png")
plt.close

# 3. Matrix Plot --> heatmap

numeric_cols = ["Quantity", "UnitPrice", "Discount_pct", "ShippingCost", "TotalAmount", "Rating"]
correlation_matrix = df[numeric_cols].corr()

plt.figure(figsize=(7,6))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", center=0)

plt.title("Correlation Matrix - Numeric Columns")
plt.tight_layout()
plt.savefig("./12_matrixplot.png")
plt.close()

