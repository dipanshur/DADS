## Customer Retention and growth analysis

# Q1 - can we trust customer data ? or does it contains quality issues?
# Q2 - what does a typical customer looks like statistically?
# Q3 - Are customer groups genuinely different or are appaernt differences just random variations?
# Q4 - Which customers behave similarly?
# Q5 - Can we identify customers likely to churn so retention team can intervene?


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    recall_score,
    precision_score,
    f1_score,
    confusion_matrix,
    roc_auc_score,
)

# rows --> observations, columns --> features

df_raw = pd.read_csv("./data_science_master_course_dataset.csv")
print(df_raw.shape)

# print(df_raw.head(5))
# print(df_raw.columns.tolist())
# print(df_raw.info())

print(df_raw.duplicated().sum())
df = df_raw.drop_duplicates().copy()
print(df.shape)

missing = df.isnull().sum().sort_values(ascending=False)

print(missing.head(10))

invalid_age = df[(df["customer_age"] < 18) | (df["customer_age"] > 100)]
print(invalid_age[["customer_age", "customer_id"]])

df.loc[(df["customer_age"] < 18) | (df["customer_age"] > 100), "customer_age"] = np.nan

invalid_shipping = df["shipping_days"] <= 0
print(invalid_shipping.sum())

df.loc[df["shipping_days"] <= 0, "shipping_days"] = np.nan

invalid_discount = (df["discount_pct"] < 0) | (df["discount_pct"] > 100)
print(invalid_discount.sum())

# print(df["city"].value_counts())

df["city"] = df["city"].astype("string").str.strip().str.title()
print(df["city"].value_counts())

df["membership_tier"] = df["membership_tier"].astype("string").str.strip().str.title()

df["payment_method"] = (
    df["payment_method"]
    .astype("string")
    .str.strip()
    .str.replace("_", " ", regex=False)
    .str.title()
)

df["product_category"] = df["product_category"].astype("string").str.strip().str.title()

print(df["city"].value_counts())


columns = ["total_spend_12m", "annual_income", "previous_orders", "satisfaction_score"]

print(df[columns].describe().round(2))

plt.hist(df["total_spend_12m"], bins=20)
plt.xlabel("Total Spend (12 Months)")
plt.ylabel("Customers")
plt.title("Customer Spending Distribution of Total Spend 12m")
# plt.show()

print(df["total_spend_12m"].skew())  ## mean >> median, right skewed distribution

spend_range = df["total_spend_12m"].max() - df["total_spend_12m"].min()
print(round(spend_range, 2))

variance = df["total_spend_12m"].var()
print(round(variance, 2))


customer_a = df.iloc[0]
customer_b = df.iloc[1]

distance = np.sqrt(
    (customer_a["customer_age"] - customer_b["customer_age"]) ** 2
    + (customer_a["previous_orders"] - customer_b["previous_orders"]) ** 2
)

print(round(distance, 2))

# ~~~ order age spending == 35410.18

distance_features = ["customer_age", "previous_orders", "total_spend_12m"]

X_distance = df[distance_features]
imputer = SimpleImputer(strategy="mean")
X_distance_imputed = imputer.fit_transform(X_distance)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_distance_imputed)

scaled_distance = np.linalg.norm(X_scaled[0] - X_scaled[1])
print(round(scaled_distance, 2))

## population and sample

# 2500 is population size.

sample = df.sample(n=500, random_state=42)

print(round(df["total_spend_12m"].mean(), 2))
print(round(sample["total_spend_12m"].mean(), 2))
sample_mean = round(sample["total_spend_12m"].mean(), 2)

sample_spend = sample["total_spend_12m"].dropna()

standard_error = stats.sem(sample_spend)

ci = stats.t.interval(
    confidence=0.95, df=len(sample_spend) - 1, loc=sample_mean, scale=standard_error
)

print(round(ci[0], 2), (round(ci[1], 2)))

# Q -  Do pune customers spend more or less than mumbai customers?

Pune = df.loc[df["city"] == "Pune", "total_spend_12m"].dropna()
Mumbai = df.loc[df["city"] == "Mumbai", "total_spend_12m"].dropna()

print("Pune:", round(Pune.mean(), 2))
print("Mumbai:", round(Mumbai.mean(), 2))

## H0 Null Hypothesis: Pune customers spend the same as Mumbai customers
## Average spend of Pune  = Average spend of Mumbai

## H1 Alternative Hypothesis: Pune customers spend more than Mumbai customers
## Average spend of Pune  != Average spend of Mumbai

# 1. Welch t-test --> does not assume equal variance between the two groups
t_stat, p_value = stats.ttest_ind(Pune, Mumbai, equal_var=False)

print(
    round(t_stat, 2), round(p_value, 4)
)  # p>0.05 --> fail to reject H0 --> Pune customers spend the same as Mumbai customers

## features --> model --> churn
## Supervised learning --> classification --> Binary classification
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

target = "churned_90d"  # 0 -- did not, 1 - churned

x = df[features]
y = df[target]

print(y.value_counts())
print(x.value_counts(normalize=True))

## Training data  --> teaches the model

X_train, X_test, Y_train, Y_test = train_test_split(
    x, y, test_size=0.20, random_state=42, stratify=y
)

print("Training Observation = ", len(X_train))
print("Testing Observation = ", len(X_test))
# I will predict churn only when I am extremly confident
model = Pipeline(
    [
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=1000)),
    ]
)


# missing data --> median Imputation --> feature Scaling --> LogisticRegression

model.fit(
    X_train, Y_train
)  # where learning occurs ## features + Correct Historicl targets

predictions = model.predict(X_test)

probabilities = model.predict_proba(X_test)[:, 1]
print(probabilities[:5])


print("Accuracy: ", accuracy_score(Y_test, predictions))
print("Precisions: ", precision_score(Y_test, predictions))
print("Recall: ", recall_score(Y_test, predictions))
print("F1: ", f1_score(Y_test, predictions))
print("ROC-AUC: ", roc_auc_score(Y_test, predictions))

print(confusion_matrix(Y_test, predictions))
# Stay
# True Negative = 469
# False Negative = 0

# Churn
# False Negative = 27
# True Negative = 4

baseline_prediction = np.zeros(len(Y_test))
print(accuracy_score(Y_test, baseline_prediction))

# Finding churners is important so I will be more aggresive
balanced_model = Pipeline(
    [
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced")),
    ]
)

balanced_model.fit(X_train, Y_train)

balanced_prediction = balanced_model.predict(X_test)

balanced_probabilities = balanced_model.predict_proba(X_test)[:, 1]

print("Balanced Accuracy: ", accuracy_score(Y_test, balanced_prediction))
print("Balanced Precisions: ", precision_score(Y_test, balanced_prediction))
print("Balanced Recall: ", recall_score(Y_test, balanced_prediction))
print("Balanced F1: ", f1_score(Y_test, balanced_prediction))
print("Balanced ROC-AUC: ", roc_auc_score(Y_test, balanced_probabilities))

print(confusion_matrix(Y_test, balanced_prediction))

print("\n------ FINAL MODEL COMPARISON ------")

print("Normal Model")
print("Accuracy:", round(accuracy_score(Y_test, predictions), 3))

print("Recall:", round(recall_score(Y_test, predictions), 3))

print("ROC-AUC:", round(roc_auc_score(Y_test, probabilities), 3))


print("\nBalanced Model")

print("Accuracy:", round(accuracy_score(Y_test, balanced_prediction), 3))

print("Recall:", round(recall_score(Y_test, balanced_prediction), 3))

print("ROC-AUC:", round(roc_auc_score(Y_test, balanced_probabilities), 3))


### Stay = 2347, Churn = 153 ~ 6.12%

customer_predictions = df.loc[X_test.index, ["customer_id", *features]].copy()

customer_predictions["actual_churn"] = Y_test.values

customer_predictions["predicted_churn"] = balanced_prediction
customer_predictions["churn_probablity"] = balanced_probabilities

print(customer_predictions.sort_values("churn_probablity", ascending=False).head(20))

# LogisticRegression => Churn Score --> Intercept + Age + Orders + Spending + Inactivity + Support + Return rate + satisfaction + engagement

classifier = (balanced_model.named_steps["classifier"])

coefficients = pd.Series(classifier.coef_[0], index=features)

print(coefficients.sort_values(ascending=False))

#CUST01222

# customer_index = (customer_predictions[customer_predictions["customer_id"] == "CUST01222"].index[0])

customer_index = customer_predictions.loc[
    customer_predictions["customer_id"] == "CUST02379"
].index[0]

one_customer = X_test.loc[[customer_index]]

customer_imputer = balanced_model.named_steps["imputer"]
customer_scaler = balanced_model.named_steps["scaler"]
customer_imputed = customer_imputer.transform(one_customer)
customer_scaled = customer_scaler.transform(customer_imputed)[0]
contributions = customer_scaled * classifier.coef_[0]

explaination = pd.DataFrame(
    {
        "Feature": features,
        "Original_Value": one_customer.iloc[0].values,
        "Coefficient": classifier.coef_[0],
        "Contributions": contributions,
    }
)

print(explaination.round(3))

similarity_features = [
    "customer_age", "previous_orders", "total_spend_12m"
]

similarity_data = df[similarity_features].copy()

similarity_imputer = SimpleImputer(strategy="median")
similarity_imputed = (similarity_imputer.fit_transform(similarity_data))

similarity_scaler = StandardScaler()

similarity_scaled = (similarity_scaler.fit_transform(similarity_imputed))

# CUST02292

target_position = (df.index.get_loc(df[df["customer_id"] == "CUST02292"].index[0]))

distances = np.linalg.norm(similarity_scaled - similarity_scaled[target_position], axis=1)

similar_customers = df[
    [
        "customer_id", "customer_age", "previous_orders", "total_spend_12m"
    ]
].copy()

similar_customers["distance"] = distances

similar_customers = (similar_customers[similar_customers["customer_id"] != "CUST02292" ].sort_values("distance") )

print(similar_customers.head(5))


# Risk value = Churn Probality * historical customer value

customer_predictions["risk_value_score"] = (customer_predictions["churn_probablity"] * customer_predictions["total_spend_12m"])

priority_customers = (customer_predictions.sort_values("risk_value_score", ascending=False))

print(priority_customers[
    ["customer_id", "total_spend_12m", "churn_probablity", "risk_value_score"]
].head(10))

# Q - How much revenue was actually saved?