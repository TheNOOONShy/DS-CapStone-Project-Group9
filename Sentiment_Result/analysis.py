import os
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

TYPE_PRISON = 1
# Load the merged data
merged_df = pd.read_csv('final_merged_data_with_caserate.csv')

# Convert the 'Type' column to dummy variables
merged_df = pd.get_dummies(merged_df, columns=['Type'], drop_first=True)

merged_df = pd.get_dummies(merged_df, columns = ['Level'])
# print(merged_df.columns)
# print(error)

# Exclude rows where 'Type' is 'Prison'
merged_df = merged_df[merged_df['Type_Prison'] == TYPE_PRISON]
if TYPE_PRISON == 0:
    end = ['Jail']
    features = ['Week Number', 'Prison Case Number', 'Prison Death Number',  "Specific_Facility_Death_Rate", "Specific_Facility_Case_Rate"]
elif TYPE_PRISON == 1:
    end = ['Prison']
    features = ["Level_State",'Week Number',  'Prison Death Number',  "Specific_Facility_Death_Rate", "Specific_Facility_Case_Rate"]
# Define the independent variables (features) for Positive_Count for jails
independent_vars_positive_jails = features

# Add a constant term for the intercept
X_positive_jails = sm.add_constant(merged_df[independent_vars_positive_jails])

# Define the dependent variable for Positive_Count for jails
y_positive_jails = merged_df['Positive_Count']

# Fit the linear regression model for Positive_Count for jails
model_positive_jails = sm.OLS(y_positive_jails, X_positive_jails).fit()

# Save the model to a file within the "flair_regression" folder for jails only
os.makedirs('flair_regression', exist_ok=True)
filename_positive_jails = '_'.join(independent_vars_positive_jails + end)
model_positive_jails.save(os.path.join('flair_regression', f'positive_count_model_{filename_positive_jails}.pkl'))

# Print the summary of the regression for Positive_Count for jails
print(f"Linear Regression for Positive_Count (Jails only) using independent variables: {', '.join(independent_vars_positive_jails)}")
print(model_positive_jails.summary())

# Define the independent variables (features) for Negative_Count for jails
independent_vars_negative_jails = features

# Add a constant term for the intercept
X_negative_jails = sm.add_constant(merged_df[independent_vars_negative_jails])

# Define the dependent variable for Negative_Count for jails
y_negative_jails = merged_df['Negative_Count']

# Fit the linear regression model for Negative_Count for jails
model_negative_jails = sm.OLS(y_negative_jails, X_negative_jails).fit()

# Save the model to a file within the "flair_regression" folder for jails only
filename_negative_jails = '_'.join(independent_vars_negative_jails + end)
model_negative_jails.save(os.path.join('flair_regression', f'negative_count_model_{filename_negative_jails}.pkl'))

# Print the summary of the regression for Negative_Count for jails
print(f"\nLinear Regression for Negative_Count (Jails only) using independent variables: {', '.join(independent_vars_negative_jails)}")
print(model_negative_jails.summary())

# Define the independent variables (features) for Total_Count for jails
independent_vars_total_count_jails = features

# Add a constant term for the intercept
X_total_count_jails = sm.add_constant(merged_df[independent_vars_total_count_jails])

# Define the dependent variable for Total_Count for jails
y_total_count_jails = merged_df['Positive_Count'] + merged_df['Negative_Count']

# Fit the linear regression model for Total_Count for jails
model_total_count_jails = sm.OLS(y_total_count_jails, X_total_count_jails).fit()

vif_data = pd.DataFrame()
vif_data["Variable"] = X_total_count_jails.columns
vif_data["VIF"] = [variance_inflation_factor(X_total_count_jails.values, i) for i in range(X_total_count_jails.shape[1])]

# Print the results
# print("VIF for each variable:")
# print(vif_data)
# # Extract the target variable
# y = (facility_data["FlairSentiment"] == "POSITIVE").astype(int)

# Save the model to a file within the "flair_regression" folder for jails only
filename_total_count_jails = '_'.join(independent_vars_total_count_jails + end)
model_total_count_jails.save(os.path.join('flair_regression', f'total_count_model_{filename_total_count_jails}.pkl'))

# Print the summary of the regression for Total_Count for jails
print(f"\nLinear Regression for Total_Count (Jails only) using independent variables: {', '.join(independent_vars_total_count_jails)}")
print(model_total_count_jails.summary())
