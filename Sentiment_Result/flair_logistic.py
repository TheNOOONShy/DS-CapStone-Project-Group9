import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import PolynomialFeatures
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from imblearn.over_sampling import RandomOverSampler


def run_facility(facility_name, data):
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

    columns_to_include = ["case number",
    #"case rate",
    "death number",
    # "death rate", 
    "length",
    "Week Label",
    "NLTK_Compound",
    "is_covid_peak",
    "Prison or County Population"]
    # ]

    letter_call_dummy = pd.get_dummies(facility_data["Letter/Call"], prefix="LetterCall", drop_first=True)
    # for a in letter_call_dummy["LetterCall_Letter"]:
    #     print(a)
    # Combine dummy variable with other selected columns
    X = pd.concat([facility_data[columns_to_include], letter_call_dummy], axis=1)
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

    X = sm.add_constant(X)  # Add a constant term for the intercept
    X_no_const = X.copy()
    if 'const' in X_no_const:
        X_no_const = X_no_const.drop('const', axis=1)

    # Add a constant term for the intercept
    X_with_const = sm.add_constant(X_no_const)

    # Calculate VIF for each variable
    vif_data = pd.DataFrame()
    vif_data["Variable"] = X_with_const.columns
    vif_data["VIF"] = [variance_inflation_factor(X_with_const.values, i) for i in range(X_with_const.shape[1])]

    # Print the results
    print("VIF for each variable:")
    print(vif_data)
    # Extract the target variable
    y = (facility_data["FlairSentiment"] == "POSITIVE").astype(int)

    oversampler = RandomOverSampler(sampling_strategy='minority', random_state=42)
    X_resampled, y_resampled = oversampler.fit_resample(X, y)

    # Initialize the logistic regression model using statsmodels
    model = sm.Logit(y_resampled, X_resampled)

    # Fit the model to the current facility's data
    try:
        # Initialize the logistic regression model using statsmodels
        # model = sm.Logit(y, X)

        # Fit the model to the current facility's data
        result = model.fit()

        # Display the summary of the model
        print(f"Facility Name: {facility_name}")
        print(result.summary())

        # Save the results to a folder for each facility
        folder_name = "flair_regression"
        os.makedirs(folder_name, exist_ok=True)

        # Create a file name with the names of independent variables and facility name
        independent_vars_str = "_".join(X.columns)
        result_file_name = f"logistic_regression_result_{facility_name}_{independent_vars_str}_sampled.pickle"

        result.save(os.path.join(folder_name, result_file_name))
        print("\n")

    except Exception as e:
        print(f"Error fitting the model for {facility_name}: {str(e)}")

SINGLE_FACILITY = False
IS_BOTH = False
IS_PRISON = False
# Load the data
file_path = "weeklydata.csv"
data = pd.read_csv(file_path)

if SINGLE_FACILITY:
    # Loop through unique Facility Names
    for facility_name in data["Facility Name"].unique():
        run_facility(facility_name, data)
            # Optionally, you may want to add further error handling or logging here
elif IS_BOTH:
    run_facility("all", data)
elif IS_PRISON:
    run_facility("prison", data)
else:
    run_facility("jail", data)
