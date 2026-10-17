# Forecasting?? --> process of using historical data to estimate an outcome that has not happened yet.

# Prediction?? --> 

# target exist --> yes --> Supervised learning -->  number (Regression) or category (classification)

# target does not exist --> Unsupervised learning

# next_30d_spend --> Regression
# churned_90d --> classification


# Regression --> learn how changes in the input fetures are associated with changes in a numeric target

# 1. Simple linear Regression --> One case/Scenario

# X --> Previous Orders
# Y --> Future Spending

# y(predict Value) = b0(Intercept) + b1(slope/coeficient)x(input features)

# 2. Multiple linear Regresion 

# y = b0 + b1x1 + b2x2 .. + bnxn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


df = pd.read_csv("./data_science_master_course_dataset.csv")

features = [
    "previous_orders",
    "days_since_last_order",
    "page_views_30d",
    "avg_order_value_6m"
]

target = "next_30d_spend"

reg_df = df[features + [target]].dropna()

X = reg_df[features]
y = reg_df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42) 
#80 == model learn
#20 == model is evaluated

model = LinearRegression()

model.fit(X_train, y_train) ## Intercept + Coeficient

#Residual = Actual value - Predicted Value

predictions = model.predict(X_test)

print(predictions[:5].round(2))

comparision = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": predictions
})

print(comparision.head())

print("Intercept: ", model.intercept_)
coefficients = pd.DataFrame({
    "Features": features,
    "Coefficient" : model.coef_
})

print(coefficients)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, predictions)

print("On Average prediction differs from actual future spending - MAE: ", mae)
print("MSE: ", mse)
print("Error to approximatly original value - RMSE: ", rmse)
print("R2: " ,r2)

plt.scatter(y_test, predictions)

plt.xlabel("Actual Spending")
plt.ylabel("Predicted Spending")

plt.title("Actual VS Predicted")

# plt.show()

# ## Assumption
# 1. Linearity 
# 2. Independence 
# 3. Homoscedasticity
# 4. residual Normality 
# 5. limited multicollinearlity