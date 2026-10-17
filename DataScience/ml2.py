# Logistics regression -- > classification Alogirithm

# --> Sigmoid function => P = 1/(1+e^-z)  --> 0 to 1

# z = linear regression score
# z = intercept + Age + previous order + ... 

# P --> -z 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score
from sklearn.neighbors import KNeighborsClassifier


df = pd.read_csv("./data_science_master_course_dataset.csv")

features = [
    "customer_age",
    "previous_orders",
    "total_spend_12m",
    "days_since_last_order",
    "support_tickets_6m",
    "return_rate_6m",
    "satisfaction_score",
    "page_views_30d",
]

target = "churned_90d"

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, stratify=y)


logistics_model = Pipeline(
    [
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced"))
    ]
)

logistics_model.fit(X_train, y_train)

logistics_predictions = logistics_model.predict(X_test)
print(logistics_predictions)

logistics_probablity = (logistics_model.predict_proba(X_test)[:,-1])
print(logistics_probablity)


print("Accuracy: ", accuracy_score(y_test, logistics_predictions))
print("Precisions: ", precision_score(y_test, logistics_predictions))
print("Recall: ", recall_score(y_test, logistics_predictions))
print("F1: ", f1_score(y_test, logistics_predictions))
print("ROC-AUC: ", roc_auc_score(y_test, logistics_predictions))

print(confusion_matrix(y_test, logistics_predictions))

# --> KNN theory (K-Nearest Neighbour)

### Observations that are similar to each other are ofthen likely to have similar outcomes --> Assumption

## coeficient --> Equation --> probablity

##KNN --> who looks most similar to this customer?

# k = Number of nearest neighbours considers?

# cust A --> 30, orders = 10, 50000
# cust B --> 35, orders = 15, 500000
# d= sqrt((x2-x1)sq + (y2-y1)sq + (z2-z1)sq) = 5

knn_model = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
    ("classifier",KNeighborsClassifier(n_neighbors=5))
])

knn_model.fit(X_train, y_train)

knn_prediction = (knn_model.predict(X_test))
knn_probablity = (knn_model.predict_proba(X_test)[:,-1])


print("Accuracy: ", accuracy_score(y_test, knn_prediction))
print("Precisions: ", precision_score(y_test, knn_prediction))
print("Recall: ", recall_score(y_test, knn_prediction))
print("F1: ", f1_score(y_test, knn_prediction))
print("ROC-AUC: ", roc_auc_score(y_test, knn_prediction))

print(confusion_matrix(y_test, knn_prediction))

# Small k --> complex decision Boundry --> High variance --> possible overfitting
# large k --> possible underfitting

# KNN --> Lazy Learner

# Q --> Find the most suitable KNN configuration for identifying potential churners?