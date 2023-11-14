import os
import pandas as pd
import statsmodels.api as sm

# Load the merged data
merged_df = pd.read_csv('final_merged_data.csv')

# Convert the 'Type' column to dummy variables
merged_df = pd.get_dummies(merged_df, columns=['Type'], drop_first=True)

# Exclude rows where 'Type' is 'Jail'
merged_df = merged_df[merged_df['Type_Jail'] == 0]

# Separate 'Case_Death_Number' into 'Number of Cases' and 'Number of Deaths'
merged_df['Number_of_Cases'] = merged_df['Prison Case Number']
merged_df['Number_of_Deaths'] = merged_df['Prison Death Number']

# Include the 'Level' variable
merged_df = pd.get_dummies(merged_df, columns=['Level'], drop_first=True)

# Rename columns to adjust the naming conventions
merged_df.rename(columns={'Positive_count': 'Positive_Count'}, inplace=True)

# Add a fourth-degree polynomial for 'Week Number'
merged_df['Week_Number_2'] = merged_df['Week Number'] ** 2
merged_df['Week_Number_3'] = merged_df['Week Number'] ** 3
merged_df['Week_Number_4'] = merged_df['Week Number'] ** 4

# Define the independent variables (features) for Positive_Count
independent_vars_positive = ['Week Number', 'Week_Number_2', 'Week_Number_3', 'Week_Number_4', 'Number_of_Cases', 'Number_of_Deaths', 'Level_State']

# Add a constant term for the intercept
X_positive = sm.add_constant(merged_df[independent_vars_positive])

# Define the dependent variable for Positive_Count
y_positive = merged_df['Positive_Count']

# Fit the linear regression model for Positive_Count
model_positive = sm.OLS(y_positive, X_positive).fit()

# Save the model to a file within the "flair_regression" folder for prisons only
os.makedirs('flair_regression', exist_ok=True)
filename_positive_prisons = '_'.join(independent_vars_positive + ['Prisons'])
model_positive.save(os.path.join('flair_regression', f'positive_count_model_{filename_positive_prisons}.pkl'))

# Print the summary of the regression for Positive_Count
print(f"Linear Regression for Positive_Count (Prisons only) using independent variables: {', '.join(independent_vars_positive)}")
print(model_positive.summary())

# Define the independent variables (features) for Negative_Count
independent_vars_negative = ['Week Number', 'Week_Number_2', 'Week_Number_3', 'Week_Number_4', 'Number_of_Cases', 'Number_of_Deaths', 'Level_State']

# Add a constant term for the intercept
X_negative = sm.add_constant(merged_df[independent_vars_negative])

# Define the dependent variable for Negative_Count
y_negative = merged_df['Negative_Count']

# Fit the linear regression model for Negative_Count
model_negative = sm.OLS(y_negative, X_negative).fit()

# Save the model to a file within the "flair_regression" folder for prisons only
filename_negative_prisons = '_'.join(independent_vars_negative + ['Prisons'])
model_negative.save(os.path.join('flair_regression', f'negative_count_model_{filename_negative_prisons}.pkl'))

# Print the summary of the regression for Negative_Count
print(f"\nLinear Regression for Negative_Count (Prisons only) using independent variables: {', '.join(independent_vars_negative)}")
print(model_negative.summary())

# Define the independent variables (features) for Total_Count
independent_vars_total_count = ['Week Number', 'Week_Number_2', 'Week_Number_3', 'Week_Number_4', 'Number_of_Cases', 'Number_of_Deaths', 'Level_State']

# Add a constant term for the intercept
X_total_count = sm.add_constant(merged_df[independent_vars_total_count])

# Define the dependent variable for Total_Count
y_total_count = merged_df['Positive_Count'] + merged_df['Negative_Count']

# Fit the linear regression model for Total_Count
model_total_count = sm.OLS(y_total_count, X_total_count).fit()

# Save the model to a file within the "flair_regression" folder for prisons only
filename_total_count_prisons = '_'.join(independent_vars_total_count + ['Prisons'])
model_total_count.save(os.path.join('flair_regression', f'total_count_model_{filename_total_count_prisons}.pkl'))

# Print the summary of the regression for Total_Count
print(f"\nLinear Regression for Total_Count (Prisons only) using independent variables: {', '.join(independent_vars_total_count)}")
print(model_total_count.summary())
