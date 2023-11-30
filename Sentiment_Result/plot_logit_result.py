import os
import pickle
import statsmodels.api as sm
import matplotlib.pyplot as plt
import math
import numpy as np

def round_to_sf(x, sf):
    # Custom rounding function for significant figures
    if x == 0:
        return 0
    else:
        return round(x, -int(math.floor(math.log10(abs(x)))) + (sf - 1))

def map_labels(original_labels):
    label_mapping = {
        'Week_Number_4': 'Week Number^4',
        'Week_Number_3': 'Week Number^3',
        'Week_Number_2': 'Week Number^2',
        'Week_Number_1': 'Week Number',
        "death number": "Weekly Deaths",
        "Type_Prison": "Is Prison",
        "case number": "Weekly Cases",
        "Level_State": "Is State Prison",
        "Number_of_Deaths": "Weekly Deaths",
        "Number_of_Cases": "Weekly Cases",
        "Week Label": "Week Number",
        "case rate": "Weekly Case Rate",
        "death rate": "Weekly Death Rate",
        "NLTK_Compound": "Vader Score",
        "is_covid_peak": "Is Covid Peak",
        "LetterCall_Letter": "Is Letter",
        "length": "Length (chars)",
        "Level_Federal": "Is Federal Prison",
        "Type_case number": "Weekly Prison Case Number",
        "Type_death number": "Weekly Prison Death Number",
        "Specific_Facility_Case_Rate": "Weekly Case Rate",
        "Specific_Facility_Death_Rate": "Weekly Death Rate",
        "Prison Death Number": "Weekly Death Number",
        "Prison Case Number": "Weekly Case Number",
        "Prison or County Population": "Size"
        # Add more mappings as needed
    }
    return [label_mapping.get(label, label) for label in original_labels]

def plot(file):
    try:
        # Try to open the file using pickle
        with open(file_path, 'rb') as file:
            # Load the model using sm.load
            data = sm.load(file_path)

            # Extract coefficients, p-values, and R-squared
            coefficients = data.params.apply(lambda x: round_to_sf(x, 4))
            # print(coefficients.index)
            # Map original labels to human-readable labels
            readable_labels = map_labels(list(coefficients.index), label_mapping)
            # print('here')

            p_values = data.pvalues
            if hasattr(data, 'rsquared_adj'):
                r_squared = data.rsquared_adj
                if "negative_count" in file_path:
                    title_text = f'Weekly Negative Count Results (R-squared: {r_squared:.4f})'
                elif "positive" in file_path:
                    title_text = f'Weekly Positive Count Results (R-squared: {r_squared:.4f})'
                elif "total_count" in file_path:
                    title_text = f'Weekly Total Count Results (R-squared: {r_squared:.4f})'
            elif hasattr(data, 'prsquared'):
                r_squared = data.prsquared
                title_text = f'Logistic Regression Results (Pseudo-R-squared: {r_squared:.4f})'

            if "jail" in file_path or "Jails" in file_path:
                title_text += " (jail)"
            elif "prison" in file_path or "Prisons" in file_path:
                title_text += " (prison)"

            # Plot negative log p-values for each variable
            plt.figure(figsize=(12, len(coefficients) * 0.8))  # Adjust figure size
            labels = [readable_labels[i] + ' (' + coefficients.astype(str)[i] + ')' for i in range(len(readable_labels))]
            bars = plt.barh(labels, -1 * np.log(p_values), color='skyblue')
            plt.axvline(x=abs(np.log(0.1)), color='r', linestyle='--', label='p-value = 0.1')
            plt.axvline(x=abs(np.log(0.05)), color='g', linestyle='--', label='p-value = 0.05')
            plt.xlabel('Negative log p-value')
            plt.title(title_text)
            plt.legend()
            plt.tight_layout()  # Adjust layout to prevent label cutoff

            # Add actual p-value labels to the right of the bars, outside of the bars
            for bar, p_value, readable_label in zip(bars, p_values, readable_labels):
                plt.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height() / 2, f'{p_value:.4f}', ha='left', va='center', color='black')

            # Save the plot to a file with the same name as the data file
            plt.savefig(os.path.splitext(file_path)[0] + '.png')

            # Close the interactive display
            plt.close()

    except Exception as e:
        # Print an error message if the file cannot be opened
        print(f"{file_name} cannot be opened. Error: {e}")

folder_path = "flair_regression"


# Get a list of all files in the folder
file_list = [f for f in os.listdir(folder_path) if f.endswith(".pkl") or f.endswith(".pickle")]

# Iterate through each file
for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)

    plot(file_path)
