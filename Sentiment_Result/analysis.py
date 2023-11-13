import os
import pandas as pd
import statsmodels.api as sm

# Load the merged data
merged_df = pd.read_csv('final_merged_data.csv')

# Convert the 'Type' column to dummy variables
merged_df = pd.get_dummies(merged_df, columns=['Type'], drop_first=True)

# Create the combined variable 'Case_Death_Number'
merged_df['Case_Death_Number'] = merged_df['Prison Case Number'] + merged_df['Prison Death Number']

# Include the 'Level' variable
merged_df = pd.get_dummies(merged_df, columns=['Level'], drop_first=True)

# Rename columns to adjust the naming conventions
merged_df.rename(columns={'Type_jail': 'Type_Jail', 'Positive_count': 'Positive_Count'}, inplace=True)

# Define the independent variables (features) for Positive_Count
independent_vars_positive = ['Week Number', 'Overall Count_x', 'Type_Jail', 'Case_Death_Number', 'Level_State', 'Level_Federal']

# Add a constant term for the intercept
X_positive = sm.add_constant(merged_df[independent_vars_positive])

# Define the dependent variable for Positive_Count
y_positive = merged_df['Positive_Count']

# Fit the linear regression model for Positive_Count
model_positive = sm.OLS(y_positive, X_positive).fit()

# Save the model to a file within the "flair_regression" folder
os.makedirs('flair_regression', exist_ok=True)
filename_positive = '_'.join(independent_vars_positive)
model_positive.save(os.path.join('flair_regression', f'positive_count_model_{filename_positive}.pkl'))

# Print the summary of the regression for Positive_Count
print(f"Linear Regression for Positive_Count using independent variables: {', '.join(independent_vars_positive)}")
print(model_positive.summary())

# Define the independent variables (features) for Negative_Count
independent_vars_negative = ['Week Number', 'Overall Count_x', 'Type_Jail', 'Case_Death_Number', 'Level_State', 'Level_Federal']

# Add a constant term for the intercept
X_negative = sm.add_constant(merged_df[independent_vars_negative])

# Define the dependent variable for Negative_Count
y_negative = merged_df['Negative_Count']

# Fit the linear regression model for Negative_Count
model_negative = sm.OLS(y_negative, X_negative).fit()

# Save the model to a file within the "flair_regression" folder
filename_negative = '_'.join(independent_vars_negative)
model_negative.save(os.path.join('flair_regression', f'negative_count_model_{filename_negative}.pkl'))

# Print the summary of the regression for Negative_Count
print(f"\nLinear Regression for Negative_Count using independent variables: {', '.join(independent_vars_negative)}")
print(model_negative.summary())

# Define the independent variables (features) for Total_Count
independent_vars_total_count = ['Week Number', 'Overall Count_x', 'Type_Jail', 'Case_Death_Number', 'Level_State', 'Level_Federal']

# Add a constant term for the intercept
X_total_count = sm.add_constant(merged_df[independent_vars_total_count])

# Define the dependent variable for Total_Count
y_total_count = merged_df['Positive_Count'] + merged_df['Negative_Count']

# Fit the linear regression model for Total_Count
model_total_count = sm.OLS(y_total_count, X_total_count).fit()

# Save the model to a file within the "flair_regression" folder
filename_total_count = '_'.join(independent_vars_total_count)
model_total_count.save(os.path.join('flair_regression', f'total_count_model_{filename_total_count}.pkl'))

# Print the summary of the regression for Total_Count
print(f"\nLinear Regression for Total_Count using independent variables: {', '.join(independent_vars_total_count)}")
print(model_total_count.summary())
