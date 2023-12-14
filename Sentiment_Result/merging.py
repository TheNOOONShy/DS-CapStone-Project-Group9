import pandas as pd
import os
# Load the CSV files into DataFrames
# ratio_df = pd.read_csv('weekly_ratio_by_prison.csv')
# death_case_df = pd.read_csv('weeklyDeathCaseByPrison.csv')
#
# # Merge the DataFrames based on "Facility Name" and "Week Number"
# merged_df = pd.merge(ratio_df, death_case_df, on=['Facility Name', 'Week Number'], how='outer', indicator=True)
#
# # Filter rows that are only in one of the original DataFrames
# unmerged_rows = merged_df[merged_df['_merge'] != 'both']
#
# # Save the merged DataFrame to a new CSV file
# merged_df.to_csv('merged_data.csv', index=False)
#
# # Save the unmerged rows to a new CSV file
# unmerged_rows.to_csv('unmerged_data.csv', index=False)
#
# # Print the unmerged rows
# print("Unmerged Rows:")
# print(unmerged_rows)

# # Load the merged weekly data
# merged_df = pd.read_csv('merged_weekly_data.csv')
#
# # Load the NewLocation data
# new_location_df = pd.read_csv(os.path.join('datamayneed', 'NewLocation.csv'))
#
# # Merge the dataframes based on "Facility Name" and "Type"
# final_merged_df = pd.merge(merged_df, new_location_df, how='left', left_on=['Facility Name', 'Type'], right_on=['Location', 'Type'])
#
# # Drop the duplicate "Facility Name" and "Type" columns from the NewLocation dataframe
# final_merged_df.drop(['Location'], axis=1, inplace=True)
#
# # Save the final merged dataframe
# final_merged_df.to_csv('final_merged_data.csv', index=False)
#
# # Display the first few rows of the final merged dataframe
# print(final_merged_df.head())

# Load the final merged data
import pandas as pd

# Load the merged data
final_merged_data = pd.read_csv('final_merged_data.csv')

# Load the weekly death case rate data
weekly_death_caserate_data = pd.read_csv('weeklyDeathCaserate.csv')

# Drop the 'Type' column from weeklyDeathCaserate
weekly_death_caserate_data.drop(columns=['Type'], inplace=True, errors='ignore')

# Merge the dataframes on 'Facility Name' and 'Week Number'
merged_data = pd.merge(final_merged_data, weekly_death_caserate_data, on=['Facility Name', 'Week Number'], how='inner')

# Save the merged data to a new CSV file
merged_data.to_csv('final_merged_data_with_caserate.csv', index=False)
