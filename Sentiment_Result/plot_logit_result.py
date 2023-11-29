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

folder_path = "flair_regression"

# Get a list of all files in the folder
file_list = [f for f in os.listdir(folder_path) if f.endswith(".pkl") or f.endswith(".pickle")]

# Iterate through each file
for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)

    try:
        # Try to open the file using pickle
        with open(file_path, 'rb') as file:
            # Load the model using sm.load
            data = sm.load(file_path)

            # Extract coefficients, p-values, and R-squared
            coefficients = data.params.apply(lambda x: round_to_sf(x, 4))
            p_values = data.pvalues
            r_squared = data.rsquared if hasattr(data, 'rsquared') else data.prsquared

            # Plot negative log p-values for each variable
            plt.figure(figsize=(12, len(coefficients) * 0.8))  # Adjust figure size
            bars = plt.barh(coefficients.index + ' (' + coefficients.astype(str) + ')', -1 * np.log(p_values), color='skyblue')
            plt.axvline(x=abs(np.log(0.1)), color='r', linestyle='--', label='p-value = 0.1')
            plt.axvline(x=abs(np.log(0.05)), color='g', linestyle='--', label='p-value = 0.05')
            plt.xlabel('Negative log p-value')
            plt.title(f'P-values and R-squared (R-squared: {r_squared:.4f})')
            plt.legend()
            plt.tight_layout()  # Adjust layout to prevent label cutoff

            # Add actual p-value labels to the right of the bars, outside of the bars
            for bar, p_value in zip(bars, p_values):
                plt.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height() / 2, f'{p_value:.4f}', ha='left', va='center', color='black')

            # Save the plot to a file with the same name as the data file
            plt.savefig(os.path.splitext(file_path)[0] + '.png')

            # Close the interactive display
            plt.close()

    except Exception as e:
        # Print an error message if the file cannot be opened
        print(f"{file_name} cannot be opened. Error: {e}")
