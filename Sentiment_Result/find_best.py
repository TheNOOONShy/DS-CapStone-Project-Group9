import os
import statsmodels.api as sm

folder_path = 'flair_regression'

# Dictionary to store top adjusted R-squared values for each group and subgroup
model_results = {'negative_count': {'Prisons': None, 'Jails': None, 'all': None},
                 'positive_count': {'Prisons': None, 'Jails': None, 'all': None},
                 'total_count': {'Prisons': None, 'Jails': None, 'all': None}}

# Iterate through files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".pkl"):
        file_path = os.path.join(folder_path, filename)

        # Load the saved model
        loaded_model = sm.load(file_path)

        # Extract adjusted R-squared value from the summary
        adj_r_squared = loaded_model.rsquared_adj

        # Categorize files based on their prefixes and endings
        if filename.startswith("negative_count"):
            if filename.endswith("_Prisons.pkl") and (model_results['negative_count']['Prisons'] is None or
                                                      adj_r_squared > model_results['negative_count']['Prisons']):
                model_results['negative_count']['Prisons'] = adj_r_squared

            elif filename.endswith("_Jails.pkl") and (model_results['negative_count']['Jails'] is None or
                                                       adj_r_squared > model_results['negative_count']['Jails']):
                model_results['negative_count']['Jails'] = adj_r_squared

            elif model_results['negative_count']['all'] is None or adj_r_squared > model_results['negative_count']['all']:
                model_results['negative_count']['all'] = adj_r_squared

        elif filename.startswith("positive_count"):
            if filename.endswith("_Prisons.pkl") and (model_results['positive_count']['Prisons'] is None or
                                                      adj_r_squared > model_results['positive_count']['Prisons']):
                model_results['positive_count']['Prisons'] = adj_r_squared

            elif filename.endswith("_Jails.pkl") and (model_results['positive_count']['Jails'] is None or
                                                       adj_r_squared > model_results['positive_count']['Jails']):
                model_results['positive_count']['Jails'] = adj_r_squared

            elif model_results['positive_count']['all'] is None or adj_r_squared > model_results['positive_count']['all']:
                model_results['positive_count']['all'] = adj_r_squared

        elif filename.startswith("total_count"):
            if filename.endswith("_Prisons.pkl") and (model_results['total_count']['Prisons'] is None or
                                                      adj_r_squared > model_results['total_count']['Prisons']):
                model_results['total_count']['Prisons'] = adj_r_squared

            elif filename.endswith("_Jails.pkl") and (model_results['total_count']['Jails'] is None or
                                                       adj_r_squared > model_results['total_count']['Jails']):
                model_results['total_count']['Jails'] = adj_r_squared

            elif model_results['total_count']['all'] is None or adj_r_squared > model_results['total_count']['all']:
                model_results['total_count']['all'] = adj_r_squared

# Print the top adjusted R-squared values for each group and subgroup
for group_name, subgroups in model_results.items():
    for subgroup_name, result in subgroups.items():
        print(f"Group: {group_name}, Subgroup: {subgroup_name}, Top Adjusted R-squared: {result}")
