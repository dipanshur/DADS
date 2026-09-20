# Devide data into train and test splits for ML

# split the data into two sets = Training SET + Test SET

# Training set = the data the model actually leans from and it is used to fit the model's parameters. The model uses this data to learn patterns, relationships, and make predictions.
# Test set = the data that model has never seen before. It is used to evaluate the model's performance and generalization ability. The test set helps assess how well the model can make predictions on new, unseen data.
## TotalAMount = Target/label, order Details = Features


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("./ecommerce_orders.csv")
df = df.drop_duplicates()

# 1. Spaerate the Features (X) from the Target (Y)

feature_cols = ["Quantity",	"UnitPrice", "Discount_pct", "ShippingCost"]
X = df[feature_cols]
Y = target_col = df["TotalAmount"]

# 2. Split the data into training and test sets
# train_test_split() --> shuffles the rows and split them into two groups (train and test) based on the specified test_size (default = 0.25)
# test_size = 0.2 --> 20% of the data will be used for testing, and the remaining 80% will be used for training.
# random_state = 42 --> ensures that the split is reproducible, meaning that every time you run the code with the same random_state, you will get the same train-test split.

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.9, random_state=42)

print(f"Training set size: {len(X_train)} rows ({len(X_train)/len(X)*100:.0f}%)")
print(f"Test set size: {len(X_test)} rows ({len(X_test)/len(X)*100:.0f}%)")

# 3.  Scale Fit on training data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Training Data - mean after scaling: ")
print(pd.DataFrame(X_train_scaled, columns=feature_cols).mean().round(10))

print(f"Test Data - mean after scaling: ")
print(pd.DataFrame(X_test_scaled, columns=feature_cols).mean().round(3))
