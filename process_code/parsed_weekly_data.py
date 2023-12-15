
import pandas as pd
from datetime import datetime
import re

def parse_file_name(file_name):
    """
    Parse the file name to extract facility name and date.
    Facility name is extracted from the start of the file name until the first digit.
    Date is extracted from the first digit until the next underscore.
    """
    first_digit_pos = next((i for i, c in enumerate(file_name) if c.isdigit()), None)
    facility_name = file_name[:first_digit_pos].rstrip('_')
    date_str = file_name[first_digit_pos:first_digit_pos + 8]
    date = datetime.strptime(date_str, '%Y%m%d').date()
    return facility_name, date

def main():
    file_path = 'weeklydata.csv' # Replace with your file path
    data = pd.read_csv(file_path)
    data['Facility Name'], data['Date'] = zip(*data['file_name'].map(parse_file_name))
    # Save the updated data back to the CSV file
    data.to_csv(file_path, index=False)
    print("Updated data saved to", file_path)

if __name__ == "__main__":
    main()
