import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import PolynomialFeatures
import os

# Load the data
file_path = "weeklydata.csv"
data = pd.read_csv(file_path)

# Specify columns for X (excluding rates, "Percent Occupied" and "Type_Jail")
columns_to_include = ["case number", "death number"]

# Create dummy variables for the "Type" and "Level" columns
type_dummies = pd.get_dummies(data["Type"], prefix="Type", drop_first=True)
level_dummies = pd.get_dummies(data["Level"], prefix="Level", drop_first=True)

# Combine dummy variables with other selected columns
X = pd.concat([data[columns_to_include], type_dummies, level_dummies], axis=1)

# Add interaction terms between "Type" and numeric variables
interaction_cols = ["case number", "death number"]
for col in interaction_cols:
    X[f"Type_{col}"] = X[f"Type_Prison"] * X[col]

# Drop the "Type_Jail" column
X = X.drop("Type_Jail", axis=1)

# Add polynomial features for "Week Number" with degree 4
poly = PolynomialFeatures(degree=4, include_bias=False)
week_number_poly = poly.fit_transform(data[["Week Number"]])
week_number_poly_df = pd.DataFrame(week_number_poly, columns=[f"Week_Number_{i}" for i in range(1, 5)])
X = pd.concat([X, week_number_poly_df], axis=1)

X = sm.add_constant(X)  # Add a constant term for the intercept

# Extract the target variable
y = (data["FlairSentiment"] == "POSITIVE").astype(int)

# Initialize the logistic regression model using statsmodels
model = sm.Logit(y, X)

# Fit the model to the entire dataset
result = model.fit()

# Display the summary of the model
print(result.summary())

# Save the results to a folder
folder_name = "flair_regression"
os.makedirs(folder_name, exist_ok=True)

# Create a file name with the names of independent variables
independent_vars_str = "_".join(X.columns)
result_file_name = f"logistic_regression_result_{independent_vars_str}.pickle"

result.save(os.path.join(folder_name, result_file_name))
