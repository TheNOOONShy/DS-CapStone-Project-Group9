import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from imblearn.over_sampling import RandomOverSampler
from xgboost import XGBClassifier, plot_importance

SINGLE_FACILITY = False
IS_BOTH = False
IS_PRISON = True

def run_facility_xgboost(facility_name, data):
    facility_data = data
    if facility_name == "prison":
        # print(data["Type"]=="Prison")
        facility_data = data[data["Type"]=="Prison"]
        # print(len(facility_data))
    elif facility_name == "jail":
        facility_data = data[data["Type"]=="Jail"]

    elif facility_name != "all":
        facility_data = data[data["Facility Name"] == facility_name]
        y = (facility_data["FlairSentiment"] == "POSITIVE").astype(int)

        # Check if there is at least one row with positive sentiment
        if y.sum() == 0:
            print(f"Skipping {facility_name} as there is no row with 'FlairSentiment' equal to 'POSITIVE'.")
            return

            # Check if there are at least 8 rows for the current facility
        elif len(facility_data) < 8:
            print(f"Skipping {facility_name} as it has less than 8 rows.")
            return
        elif len(facility_data['Week Label'].unique()) < 2:
            print(f"Skipping {facility_name} as it does not have 2 different weeks of data")
    # Specify columns for X (including "Letter/Call", "length", and excluding rates, "Percent Occupied", and "Type_Jail")

    columns_to_include = ["case number", "case rate","death number", "death rate", "length", "Week Label","NLTK_Compound","is_covid_peak", "is_call"]

    # for a in letter_call_dummy["LetterCall_Letter"]:
    #     print(a)
    # Combine dummy variable with other selected columns
    X = facility_data[columns_to_include]
    # X['Week Label 2'] = X['Week Label']* X['Week Label']
    # X['Week Label 3'] = X['Week Label']* X['Week Label']* X['Week Label']
    # X['Week Label 4'] = X['Week Label']* X['Week Label']* X['Week Label']* X['Week Label']

    if facility_name in ['prison', 'all', 'jail']:
        correlation_matrix = X.corr()

        # Create a heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
        plt.title("Correlation Matrix Heatmap")
        plt.show()
    # Combine dummy variables with other selected columns
    # X = pd.concat([facility_data[columns_to_include], type_dummies], axis=1)

    # Add polynomial features for "Week Number" with degree 4
    # poly = PolynomialFeatures(degree=4, include_bias=False)
    # week_number_poly = poly.fit_transform(facility_data[["Week Label"]])
    # week_number_poly_df = pd.DataFrame(week_number_poly, columns=[f"Week_Number_{i}" for i in range(1, 5)])
    # X = pd.concat([X, week_number_poly_df], axis=1)

    y = (facility_data["FlairSentiment"] == "POSITIVE").astype(int)

    oversampler = RandomOverSampler(sampling_strategy='minority', random_state=42)
    X_resampled, y_resampled = oversampler.fit_resample(X, y)

    # Initialize the XGBoost model
    model = XGBClassifier()

    # Fit the model to the current facility's data
    try:
        result = model.fit(X_resampled, y_resampled)

        # Display feature importance
        plot_importance(result, importance_type='gain')
        plt.title("XGBoost Feature Importance")
        # plt.show()

        # Save the feature importance plot to a file
        folder_name = "xgboost_feature_importance"
        os.makedirs(folder_name, exist_ok=True)
        importance_plot_file_name = f"xgboost_feature_importance_{facility_name}.png"
        plt.savefig(os.path.join(folder_name, importance_plot_file_name))

        print("\n")

    except Exception as e:
        print(f"Error fitting the XGBoost model for {facility_name}: {str(e)}")


# Load the data
file_path = "weeklydata.csv"
data = pd.read_csv(file_path)

if SINGLE_FACILITY:
    # Loop through unique Facility Names
    for facility_name in data["Facility Name"].unique():
        run_facility_xgboost(facility_name, data)
            # Optionally, you may want to add further error handling or logging here
elif IS_BOTH:
    run_facility_xgboost("all", data)
elif IS_PRISON:
    run_facility_xgboost("prison", data)
else:
    run_facility_xgboost("jail", data)
