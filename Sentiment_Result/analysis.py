import os
import pandas as pd
import statsmodels.api as sm

# Load the merged data
merged_df = pd.read_csv('final_merged_data_with_caserate.csv')

# Convert the 'Type' column to dummy variables
merged_df = pd.get_dummies(merged_df, columns=['Type'], drop_first=True)

# Exclude rows where 'Type' is 'Prison'
merged_df = merged_df[merged_df['Type_Prison'] == 0]

# Define the independent variables (features) for Positive_Count for jails
independent_vars_positive_jails = ['Week Number', 'Prison Case Number', 'Prison Death Number']

# Add a constant term for the intercept
X_positive_jails = sm.add_constant(merged_df[independent_vars_positive_jails])

# Define the dependent variable for Positive_Count for jails
y_positive_jails = merged_df['Positive_Count']

# Fit the linear regression model for Positive_Count for jails
model_positive_jails = sm.OLS(y_positive_jails, X_positive_jails).fit()

# Save the model to a file within the "flair_regression" folder for jails only
os.makedirs('flair_regression', exist_ok=True)
filename_positive_jails = '_'.join(independent_vars_positive_jails + ['Jails'])
model_positive_jails.save(os.path.join('flair_regression', f'positive_count_model_{filename_positive_jails}.pkl'))

# Print the summary of the regression for Positive_Count for jails
print(f"Linear Regression for Positive_Count (Jails only) using independent variables: {', '.join(independent_vars_positive_jails)}")
print(model_positive_jails.summary())

# Define the independent variables (features) for Negative_Count for jails
independent_vars_negative_jails = ['Week Number', 'Prison Case Number', 'Prison Death Number']

# Add a constant term for the intercept
X_negative_jails = sm.add_constant(merged_df[independent_vars_negative_jails])

# Define the dependent variable for Negative_Count for jails
y_negative_jails = merged_df['Negative_Count']

# Fit the linear regression model for Negative_Count for jails
model_negative_jails = sm.OLS(y_negative_jails, X_negative_jails).fit()

# Save the model to a file within the "flair_regression" folder for jails only
filename_negative_jails = '_'.join(independent_vars_negative_jails + ['Jails'])
model_negative_jails.save(os.path.join('flair_regression', f'negative_count_model_{filename_negative_jails}.pkl'))

# Print the summary of the regression for Negative_Count for jails
print(f"\nLinear Regression for Negative_Count (Jails only) using independent variables: {', '.join(independent_vars_negative_jails)}")
print(model_negative_jails.summary())

# Define the independent variables (features) for Total_Count for jails
independent_vars_total_count_jails = ['Week Number', 'Prison Case Number', 'Prison Death Number']

# Add a constant term for the intercept
X_total_count_jails = sm.add_constant(merged_df[independent_vars_total_count_jails])

# Define the dependent variable for Total_Count for jails
y_total_count_jails = merged_df['Positive_Count'] + merged_df['Negative_Count']

# Fit the linear regression model for Total_Count for jails
model_total_count_jails = sm.OLS(y_total_count_jails, X_total_count_jails).fit()

# Save the model to a file within the "flair_regression" folder for jails only
filename_total_count_jails = '_'.join(independent_vars_total_count_jails + ['Jails'])
model_total_count_jails.save(os.path.join('flair_regression', f'total_count_model_{filename_total_count_jails}.pkl'))

# Print the summary of the regression for Total_Count for jails
print(f"\nLinear Regression for Total_Count (Jails only) using independent variables: {', '.join(independent_vars_total_count_jails)}")
print(model_total_count_jails.summary())
