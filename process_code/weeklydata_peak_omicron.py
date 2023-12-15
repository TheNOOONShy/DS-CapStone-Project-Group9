
import pandas as pd

def main():
    # Load data
    file_path_weeklydata = 'weeklydata.csv' 
    file_path_week_peak_omicron = 'Week_Peak_Omicron.csv' 

    weeklydata = pd.read_csv(file_path_weeklydata)
    week_peak_omicron = pd.read_csv(file_path_week_peak_omicron)

    # Convert date columns to datetime objects
    weeklydata['Date'] = pd.to_datetime(weeklydata['Date'])
    week_peak_omicron['Start Date'] = pd.to_datetime(week_peak_omicron['Start Date'])
    week_peak_omicron['End Date'] = pd.to_datetime(week_peak_omicron['End Date'])

    # Merge based on date ranges
    merged_data = weeklydata.assign(key=1).merge(week_peak_omicron.assign(key=1), on='key').query(
        "Date >= `Start Date` & Date <= `End Date`").drop('key', 1)

    # Rename columns
    merged_data.rename(columns={
        'Week Label': 'Week Label',
        'Start Date': 'Start Date',
        'End Date': 'End Date',
        'is_peak': 'is_covid_peak',
        'is_Omicron': 'is_Omicron',
        'is_death_peak': 'is_death_peak'
    }, inplace=True)

    # Save the merged data to a new CSV file
    merged_data.to_csv('weeklydata.csv', index=False)
    print("Merged data with date ranges saved to weeklydata.csv")

if __name__ == "__main__":
    main()
