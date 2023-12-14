

# DS-CapStone-Project-Group9
## Objective
We are looking at transcripts from prisoners and those in jail about covid conditions within the jails and prisons. We are looking to see if there is any correlation between the sentiment of those and the condition of the ongoing pandemic.

## Sources of Data
1. Transcripts:

  Transcripts are recieved from the [Prison Pandemic](https://prisonpandemic.uci.edu) from UCI.

2. Covid Data:

  Divided into two parts: Prisons & Jails.

  The COVID data for Prison is based on the [COVID data](https://catalog.data.gov/dataset/cdcr-population-covid-19-tracking) of various prisons released by CDCR.

  The data for Jail comes from the [COVID New Case Data](https://data.ca.gov/dataset/covid-19-time-series-metrics-by-county-and-state-archived "released by the state of California") released by the state of California during the COVID pandemic.
  

## Process
1. Data Cleaning: **COMPLETED**

  Isolate only text files, and assign them to weeks of data with respect to the covid data that was recieved

2. Sentiment Analysis: **COMPLETED**

  Using two different packages for sentiment analysis (nltk and flair), find the overall sentiment of each of the files, excluding the UCI interviewer if they were there.

3. Combine data: **COMPLETED**

  Combine the data together to form a timeseries data that can be used for future analysis using statistcal methods.

4. Stats Anaysis: **COMPLETED**
  
  Conclusions were drawn using linear regression and logistic regression.


## Repository Structure
????


## How to Navigate the Repository
Instructions on how to navigate the repository, including where to find the data, how to run the scripts, and where to find the analysis and results.

## Data Dictionary

Below are descriptions of each column in the dataset:

<details>
<summary>View `Summary_Weekly.csv` Description</summary>


### `file_name`

**Description**: 
- This column is titled "File Name" and contains the names of the transcript files. Each entry in this column corresponds to a unique file, representing the source document for the associated data.

**Note**:
- This table includes only the files with names ending in `Full.txt`, indicating that it contains exclusively the complete versions of the transcripts. It does not encompass files that are fragments or other variants from the original collection provided.


### `is_call`

**Description**: 
- The column named "is_call" indicates the nature of the transcript. This column uses a binary system to differentiate between calls and letters.

**Values**: 
- In this column, a value of `1` signifies that the transcript originates from a call, whereas a value of `0` indicates that the transcript is from a letter.


### `length`

**Description**: 
- This column, labeled "length", represents the length of the transcript text. It quantifies the amount of content in each transcript.

**Measurement**: 
- The length is measured in terms of the number of characters (including spaces) or words, depending on the transcript's specific configuration.


### `Flair_Sentiment_Indicator`

 **Description**: 
- The "Flair_Sentiment_Indicator" column is a binary representation of the sentiment analysis outcomes as determined by the "FlairSentiment" column. This column simplifies the sentiment classification into a numeric format.

 **Values**: 
 - A value of `1` in this column indicates a positive sentiment, corresponding to instances where "FlairSentiment" is labeled as "POSITIVE". Conversely, a value of `0` signifies a negative sentiment, corresponding to instances where "FlairSentiment" is "NEGATIVE".


### `FlairSentiment`

**Description**: 
- The "FlairSentiment" column represents the sentiment orientation of each transcript as determined by the Flair natural language processing tool. This column categorizes the overall emotional tone conveyed in the transcript.

**Values**:  
- Sentiments in this column are typically labeled as "POSITIVE" or "NEGATIVE", reflecting the general sentiment detected in the text of the transcript. Those labels are derived from an automated sentiment analysis process.

### `FlairPolarity`

**Description**:  
- The "FlairPolarity" column quantifies the likelihood of a transcript being either positive or negative. This is represented as a numerical value, reflecting the degree of sentiment polarity detected in the transcript.

**Values**:  
- Positive numbers in this column indicate a positive sentiment, suggesting that the transcript is more likely to convey a positive tone.
- Negative numbers signify a negative sentiment, implying that the transcript is more likely to have a negative emotional context.

**Calculation**: 
- These values are the result of sentiment analysis performed by the Flair tool, which calculates the probability of the sentiment being positive or negative, based on the content of the transcript.

### `NLTK_Negative`

**Description**:  
The "NLTK_Negative" column represents the negative sentiment score of each transcript, as determined by the Natural Language Toolkit (NLTK). This score quantifies the extent of negative sentiment expressed in the transcript.

**Calculation**:  
- The score is a numerical value, calculated using NLTK's sentiment analysis tools, which assess the text to determine the presence and intensity of negative emotions or expressions.
- Higher scores in this column indicate a stronger presence of negative sentiment within the transcript.


### `NLTK_Neutral`

**Description**:  
The "NLTK_Neutral" column indicates the neutral sentiment score of each transcript, as calculated by the Natural Language Toolkit (NLTK). This score measures the level of neutral or non-emotional content present in the transcript.

**Calculation**:  
- The score is derived from NLTK's sentiment analysis capabilities, which analyze the text to gauge the extent of neutrality in the expressed sentiments.
- A higher score in this column suggests a greater presence of neutral language or a lack of strong emotional sentiment in the transcript.


### `NLTK_Positive`

**Description**:  
The "NLTK_Positive" column reflects the positive sentiment score of each transcript, as determined by the Natural Language Toolkit (NLTK). This score represents the degree to which positive emotions or attitudes are expressed in the transcript.

**Calculation**:  
- Utilizing NLTK's sentiment analysis tools, this score is computed by evaluating the text to identify and quantify expressions of positivity.
- A higher score in this column indicates a stronger presence of positive sentiment, suggesting a more optimistic or affirmative tone in the transcript.


### `NLTK_Compound`

**Description**:  
The "NLTK_Compound" column presents the compound sentiment score for each transcript, as calculated by the Natural Language Toolkit (NLTK). This score is a composite measure that encapsulates the overall sentiment expressed in the transcript, combining positive, negative, and neutral evaluations.

**Calculation**:  
- This score is derived from a holistic sentiment analysis using NLTK, where it aggregates individual sentiment scores (positive, negative, and neutral) into a single compound value.
- The compound score ranges from -1 to 1, with negative values indicating overall negative sentiment, positive values indicating overall positive sentiment, and values near zero suggesting a more neutral or balanced sentiment.


### `Date`

**Description**:  
The "Date" column is reflects the specific day when the transcript was created.

**Format**:  
- Dates are formatted in a standard date format, YYYY-MM-DD (Year-Month-Day)


### `Facility Name`

**Description**:  
The "Facility Name" column indicates the name of the facility associated with each transcript. 

**Details**:  
- The names listed in this column are as provided by the sponsors of the data.



### `CDCR Official Name`

**Description**:  
The "CDCR Official Name" column specifies the official name of the facility associated with each transcript, as used in the California Department of Corrections and Rehabilitation (CDCR) COVID Data. This name is the formal designation of the facility in CDCR records and reports.


### `Prison or County Population`

**Description**:  
The "Prison or County Population" column indicates the population relevant to the location from which each transcript originates. The population figure provided depends on whether the transcript is associated with a jail or a prison.

**Details**:  
- When a transcript originates from a jail, this column reflects the population of the corresponding county.
- Conversely, for transcripts associated with a prison, the population figure represents the inmate count of that prison as of November 2023.


### `County`

**Description**:  
The "County" column identifies the county in which the facility associated with each transcript is located.

**Details**:  
- This column lists the name of the county where each facility, whether a jail or a prison, is situated.

### `Level`

**Description**:  
The "Level" column categorizes each facility associated with the transcripts according to its administrative classification. This classification reflects the governance level of the facility, providing insight into the type of jurisdiction it falls under.

**Categories**:  
- The values in this column can be "State", "County", or "Federal", each indicating the administrative level of the facility from which the transcript originates.
- "State" refers to facilities governed at the state level.
- "County" denotes facilities that are administered by local county authorities.
- "Federal" implies facilities under the jurisdiction of the federal government.


### `Type`

**Description**:  
The "Type" column specifies the type of facility associated with each transcript. This categorization helps in identifying the nature of the institution from which the transcript was sourced.

**Categories**:  
- The column includes three primary types of facilities: "Department", "Jail", and "Prison".
- "Department" generally is "Fire Camps"
- "Jail" indicates a local detention facility typically used for short-term incarceration or for individuals awaiting trial or sentencing.
- "Prison" denotes a state or federal facility used for long-term incarceration, usually for individuals who have been convicted of a crime.

### `Week Label`

**Description**:  
The "Week Label" column is designed to correlate each record with a specific time period. This labeling facilitates the association of each record to a designated week within a defined timeframe.

**Reference Table**:  
- The column references an accompanying table named `week.csv`, which details the week assignments from December 30, 2019, to December 31, 2023.
- In this reference table, the week starting from December 30, 2019, to January 5, 2020, is labeled as "week 0". Subsequent weeks follow a natural weekly progression, each assigned a unique sequential number.


### `Start Date`

**Description**:  
The "Start Date" column denotes the beginning date of the week as identified in the "Week Label" column. It marks the first day of the specific week to which the record is attributed.

**Format**:  
- Dates are formatted in a standard date format YYYY-MM-DD (Year-Month-Day).

**Context**:  
These "Start Date"and "End Date" columns are directly tied to the "Week Label" column, providing precise date ranges for each labeled week. For instance, if a record is assigned to "week 0" in the "Week Label" column, the "Start Date" and "End Date" would correspond to the start and end dates of that particular week.



### `End Date`

**Description**:  
 The "End Date" column denotes the last day of the week in the "Week Label" column. 

**Format**:  
- Like the "Start Date", "End Date" is also formatted in a standard date format (YYYY-MM-DD) .


**Context**:  
These "Start Date"and "End Date" columns are directly tied to the "Week Label" column, providing precise date ranges for each labeled week. For instance, if a record is assigned to "week 0" in the "Week Label" column, the "Start Date" and "End Date" would correspond to the start and end dates of that particular week.
 

### `Case Number`

**Description**:  
The "Case Number" column quantifies the number of new COVID-19 cases identified within the time frame of each week as defined by the "Week Label". It reflects the total count of newly reported COVID-19 cases for that specific week.

**Context**:  
- This data is tied to the corresponding "Week Label", providing a weekly snapshot of the COVID-19 case count.
- Each value in the "Case Number" column represents the new cases that emerged during the week designated by the "Week Label".


### `Case Rate`

**Description**:  
The "Case Rate" column represents the rate of new COVID-19 cases per week, calculated as the number of new cases (from the "Case Number" column) divided by the population(from the "Population" column) .

**Calculation**:  
- For records associated with a jail, the population used in the denominator is the total population of the corresponding county.
- For records related to a prison, the population figure is the inmate count of that prison as of November 2023.


### `Death Number`

**Description**:  
The "Death Number" column indicates the total number of new COVID-19 related deaths that occurred within each week as defined by the "Week Label". This figure represents the count of newly reported fatalities due to COVID-19 for that specific week.

**Context**:  
- The data in this column is directly linked to the corresponding "Week Label", providing a weekly record of the death associated with the COVID-19 pandemic.
- Each value in the "Death Number" column reflects the number of deaths attributed to COVID-19 during the designated week.

### `Death Rate`

**Description**:  
The "Death Rate" column calculates the rate of new COVID-19 related deaths per week, obtained by dividing the number of new deaths (from the "Death Number" column) by the relevant population(from the "Population" column).

**Calculation**:  
- For records associated with a jail, the population used in the denominator is the total population of the corresponding county.
- For records related to a prison, the population figure is the inmate count of that prison as of November 2023.


### `Prison Percent Occupied`

**Description**:  
The "Prison Percent Occupied" column indicates the current occupancy rate of the prison. This rate is expressed as a percentage, calculated relative to the total designed capacity of the prison.

**Calculation**:  
- The occupancy rate is calculated as the current number of inmates divided by the prison's total capacity, multiplied by 100 to convert it into a percentage.
- An occupancy rate of 100% signifies that the prison is at its full designed capacity. 
- Rates exceeding 100% indicate that the prison is operating beyond its intended capacity.

### `IsOverCapacity`

**Description**:  
The "IsOverCapacity" column serves as an indicator of whether a prison's current occupancy rate exceeds its designed capacity. It provides a straightforward binary representation of capacity overutilization.

**Values**:  
- A value of `1` in this column signifies that the prison is operating over its designed capacity, indicating overcrowding.
- A value of `0` indicates that the prison is within or below its designed capacity.
- Empty represent cases with no data available, which most of is jail facilities.

### `OverCapacityAmount`

**Description**:  
The "OverCapacityAmount" column quantifies the extent to which a prison's current occupancy exceeds or falls short of its designed capacity. This column provides numerical values that reflect the magnitude of overcapacity or undercapacity.

**Values**:  
- Positive numbers indicate the amount by which the prison's occupancy surpasses its designed capacity, representing overcrowding situations.
- Negative numbers signify that the prison's occupancy is below its designed capacity, indicating available space.
- Empty is used where data is not available.


### `is_Covid_Peak`

**Description**:  
The "is_Covid_Peak" column indicates whether a specific week (as denoted by the "Week Label") represents a peak period of COVID-19 cases. A week is marked as a peak period (marked as 1) when the number of new COVID-19 cases in California for that week exceeds a certain threshold. This threshold is defined as the median of the weekly new cases plus the standard deviation of the weekly new cases in California's COVID-19 data.

### `is_Omicron`

**Description**:  
The "is_Omicron" column identifies the weeks that fall within the duration of the Omicron variant's prevalence, as declared by the World Health Organization (WHO). 

### `is_Death_Peak`

**Description**:  
The "is_Death_Peak" column is used to indicate whether a specific week is a peak period for COVID-19 related deaths. Similar to "is_Covid_Peak", this column marks a week as a peak death period (makes as 1) if the number of COVID-19 related deaths in that week is significantly higher than average, based on specific criteria or thresholds relevant to the mortality data.

</details>

## Acknowledgments

Special thanks to the individuals and organizations whose contributions have been instrumental in this project:

- **PrisonPandemic (Christine/Naiomi):** For providing access to prisoner communications.
- **State of California and CDCR:** For access to the public COVID-19 data that facilitated our analysis.
- **Xiang and Eileen:** For their dedication and detailed work on data preprocessing.
- **You (our team lead):** For leadership and project management.
- **Tim:** For his extensive work on model development, analysis of results, and the comprehensive writing, editing, and formatting of our final report.
- **Professor Chen Li and Pooya Khosravi:** For their support and for fostering our analytical skills.

## Data Sources

This project utilizes public data provided by:

- The State of California's COVID-19 public data repository.
- The California Department of Corrections and Rehabilitation (CDCR) for prison-specific COVID-19 statistics.

## Note on Project Privacy

This project is not open to public contribution and is intended for private use and educational purposes only. It is a collaborative effort for academic analysis under the guidance of our project sponsors and academic advisors.