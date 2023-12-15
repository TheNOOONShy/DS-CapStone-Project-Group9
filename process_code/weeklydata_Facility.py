
import pandas as pd

def main():
    # Load data
    file_path_weeklydata = 'weeklydata.csv' 
    file_path_location_facilities = 'Location_Facilities.csv' 

    weeklydata = pd.read_csv(file_path_weeklydata)
    location_facilities = pd.read_csv(file_path_location_facilities)

    # Merge the dataframes
    merged_data = pd.merge(weeklydata, location_facilities, how="left", left_on="Facility Name", right_on="Location")

    # Rename columns and select required columns
    merged_data.rename(columns={
        'Name in CDCR': 'CDCR_official_name',
        'Prison/County Population': 'Prison_or_County_Population',
        'County': 'county',
        'Level': 'Level',
        'Type': 'Type',
        'Prison Percent Occupied': 'Prison_Percent_Occupied'
    }, inplace=True)

    # Save the merged data to a new CSV file
    merged_data.to_csv('testweeklydata.csv', index=False)
    print("Merged data saved to testweeklydata.csv")

if __name__ == "__main__":
    main()
