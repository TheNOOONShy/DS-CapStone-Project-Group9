## required packages:
requirements.yml within folder (there are some that are unnessicary for this folder but those are needed to run Sentiment_result)


## Run Order
capture_info_from_redacted_full_stories.py

combine_covid_with_data_from_sponsor.py

convert_covid_data_to_weekly.py

file_lenghts.py
- for `is_call` and `length` columns

sentiment_analysis_from_folder_flair.py
- for `FlairPolarity` and `FlairSentiment` columns

sentiment_analysis_from_folder_NLTK.py
- for `NLTK_Negative` , `NLTK_Neutral`, `NLTK_Positive`, `NLTK_Compound` columns


parsed_weekly_data.py
Read `file_name`column
- for `Date`,`Facility name`columns


weeklydata_Facility.py
- Merge `weeklydata.Facility` = `Location_Facilities.Location`
- for `CDCR official Name`,`Prison or County population`,`County`,`Level`,`Type`,`Prison Percent Occupied`columns

weeklydata_peak_omicron.py
- Merge `weeklydata.date` in `Week_Peak_Omicron.Start Date` and `Week_Peak_Omicron.End Date`
- for `week label`,`Start Date`,`End Date`,`is_covid_peak`,`is_Omicron`,`is_death_peak`columns

weeklydata_cases_deaths.py
- see below.


## weeklydata_cases_deaths.py

### Overview

This script processes the 'weeklydata' dataset to calculate COVID-19 case numbers based on the type of facility. It uses two different datasets for calculation: 'Prison covid cases.csv' for prison facilities and 'covid case.csv' for other facility types.

### Functionality

#### Prison Facilities
For entries in `weeklydata.csv` where Type is "Prison", the script uses `Prison covid cases.csv`.
It matches CDCR Official Name in `weeklydata.csv` with InstitutionName in `Prison covid cases.csv`.
The script calculates the case number and death number by subtracting the TotalConfirmedcases or Totaldeaths on the Start date from the TotalConfirmed cases and Totaldeaths on the End date in `Prison covid cases`.
The calculated case number and death number are then inserted into the `weeklydata`.

#### Other Facility Types
For entries where Type is not "Prison", it uses 'covid case.csv'.
It matches county in `weeklydata` with area in `covid case`.
The script calculates the case number and the death number by summing up the cases and deaths from the Start date to the End date in `covid case`.
This calculated case number and death number is also inserted into the `weeklydata`.

#### Output
The script updates the `weeklydata` dataset with the calculated case numbers and death numbers.



## ratio.py

- for Percentage of sentiment(Flair) by Facility
### Overview

This script processes sentiment data from the `weeklydata.csv` file to calculate the weekly positive and negative sentiment ratios for each prison facility. The output is a detailed table that captures the emotional landscape of each facility on a weekly basis.

### Functionality

#### Sentiment Analysis
The script categorizes sentiment data into positive and negative counts based on the 'Flair_Sentiment_Indicator' column from `weeklydata.csv`.
Sentiments are grouped by 'Facility Name' and 'Week Label', providing a detailed breakdown of emotional responses for each facility per week.
#### Ratio Calculations

- Positive and Negative Counts: The script calculates the total number of positive and negative sentiments for each facility every week.
- Overall Sentiment Count: It computes the overall sentiment count for each week across all facilities.
- Prison Sentiment Count: The script also calculates the total number of sentiments for each prison per week.
- Sentiment Ratios: The script calculates four key ratios:
- Overall Positive Ratio: The proportion of positive sentiments out of the total sentiments for each week.
- Overall Negative Ratio: The proportion of negative sentiments out of the total sentiments for each week.
- Prison Positive Ratio: The proportion of positive sentiments in each prison per week.
- Prison Negative Ratio: The proportion of negative sentiments in each prison per week.

### Output
The script outputs a CSV file, 'ratio_by_Facility.csv', containing the calculated ratios along with the respective facility names and week labels.
The final table includes columns for positive and negative counts, overall counts, prison counts, and the calculated ratios for both overall and prison-specific sentiment analysis.

### Usage

The script requires an input CSV file (`weeklydata.csv`) containing the sentiment data.
Upon execution, it processes the data and outputs the results in `ratio_by_Facility.csv`.

## CSV files
The csv files are created elsewhere, but should not be touched, especially not final_merged_data.csv, weeklyDeathCaserate.csv, and weeklydata.csv as the first two are used by merging.py and lightgbm_importance and flair_logistic use the last one.
