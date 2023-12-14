# HOW TO RUN FILES IN FOLDER

## Required Packages
the required packages and versions are in requirements.yml

## Run Order
merging.py
analysis.py
flair_logistic.py
plot_logit_result.py
lightgbm_importance.py

## Merging.py
run python merging.py

Used to create data that analysis.py will use

## Analysis.py
run python analysis.py

`TYPE_PRISON = 1` on line 6 can be adjusted for jails or Prisons

`TYPE_PRISON = 1` is for prisons

`TYPE_PRISON = 0` is for jails

creates models that are saved into pickle form, and displays in command line
Creates 3 different models, for total sentiment count, negative sentiment counts, and positive sentiment counts

## Flair_Logistic.py
run python flair_logistic.py

on lines 12-14 (seen below) can be adjusted to identify which group we are looking at

`SINGLE_FACILITY = False #If individual facilities are wanted, will overwrites other two

IS_BOTH = False  #Combine both jail and prison, will overwrite is_prison

IS_PRISON = False  #True means prison only, False means jails only
`
creates models that are saved into pickle form, and displays in command line


##lightgbm_importance.py
(this is for XGBoost importance, bad naming of file)
run python lightgbm_importance.py

on lines 10-12 (seen below) can be adjusted to identify which group we are looking at

`SINGLE_FACILITY = False #If individual facilities are wanted, will overwrites other two

IS_BOTH = False  #Combine both jail and prison, will overwrite is_prison

IS_PRISON = False  #True means prison only, False means jails only
`

automatically saves feature importances into xgboost_feature_importance

##plot_logit_result.py

run python plot_logit_result.py

`label_mapping` on line 7 turns column names into readable feature names, items can be added as needed to dictionary via adding in the format `"column_name": "readable_label",` (please keep comma at end for consistancy)

turns the logistic regressions and linear regression pickle into negative log p-value plots

## CSV files
The csv files are created elsewhere, but should not be touched, especially not final_merged_data.csv, weeklyDeathCaserate.csv, and weeklydata.csv as the first two are used by merging.py and lightgbm_importance and flair_logistic use the last one.
