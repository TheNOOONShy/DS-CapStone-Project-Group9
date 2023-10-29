

# DS-CapStone-Project-Group9
## Objective
We are looking at transcripts from prisoners and those in jail about covid conditions within the jails and prisons. We are looking to see if there is any correlation between the sentiment of those and the condition of the ongoing pandemic.

## Sources of Data
1. Transcripts:
  Transcripts are recieved from the Prison Pandemic website from UCI
2. Covid Data:
  <NEED TO BE INSERTED>

## Process
1. Data Cleaning: **COMPLETED**

  Isolate only text files, and assign them to weeks of data with respect to the covid data that was recieved
2. Sentiment Analysis: **COMPLETED**

  Using two different packages for sentiment analysis (nltk and flair), find the overall sentiment of each of the files, excluding the UCI interviewer if they were there.
3. Combine data: **IN PROGRESS**

  Combine the data together to form a timeseries data that can be used for future analysis using statistcal methods
