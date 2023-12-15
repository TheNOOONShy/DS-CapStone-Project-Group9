
import pandas as pd

def calculate_prison_cases(weeklydata, prison_covid_cases):
    """
    Calculate the case number for prison type data.
    """
    # Convert date columns to datetime objects for comparison
    prison_covid_cases['date'] = pd.to_datetime(prison_covid_cases['date'])
    weeklydata['Start date'] = pd.to_datetime(weeklydata['Start date'])
    weeklydata['End date'] = pd.to_datetime(weeklydata['End date'])

    # Initialize an empty list to store case numbers
    case_numbers = []

    for index, row in weeklydata.iterrows():
        if row['Type'] == 'Prison':
            # Filter prison covid cases data for the specific prison and dates
            prison_cases = prison_covid_cases[
                (prison_covid_cases['InstitutionName'] == row['CDCR Official Name']) & 
                (prison_covid_cases['date'] <= row['End date']) &
                (prison_covid_cases['date'] >= row['Start date'])
            ]
            if not prison_cases.empty:
                # Calculate the case number
                case_number = prison_cases['TotalConfirmed'].iloc[-1] - prison_cases['TotalConfirmed'].iloc[0]
            else:
                case_number = 0
        else:
            case_number = None

        case_numbers.append(case_number)

    return case_numbers

def calculate_prison_death(weeklydata, prison_covid_cases):
    """
    Calculate the death_numbersr for prison type data.
    """
    # Convert date columns to datetime objects for comparison
    prison_covid_cases['date'] = pd.to_datetime(prison_covid_cases['date'])
    weeklydata['Start date'] = pd.to_datetime(weeklydata['Start date'])
    weeklydata['End date'] = pd.to_datetime(weeklydata['End date'])

    # Initialize an empty list to store death_numbers
    death_numbers = []

    for index, row in weeklydata.iterrows():
        if row['Type'] == 'Prison':
            # Filter prison covid cases data for the specific prison and dates
            prison_cases = prison_covid_cases[
                (prison_covid_cases['InstitutionName'] == row['CDCR Official Name']) & 
                (prison_covid_cases['date'] <= row['End date']) &
                (prison_covid_cases['date'] >= row['Start date'])
            ]
            if not prison_cases.empty:
                # Calculate the death_numbers
                death_numbers = prison_cases['TotalDeaths'].iloc[-1] - prison_cases['TotalDeaths'].iloc[0]
            else:
                death_numbers = 0
        else:
            death_numbers = None

        death_numbers.append(death_numbers)

    return death_numbers

def calculate_county_cases(weeklydata, covid_case):
    """
    Calculate the case number for other types (not prison).
    """
    # Convert date columns to datetime objects for comparison
    covid_case['date'] = pd.to_datetime(covid_case['date'])

    # Initialize an empty list to store case numbers
    case_numbers = []

    for index, row in weeklydata.iterrows():
        if row['Type'] != 'Prison':
            # Filter covid case data for the specific county and dates
            county_cases = covid_case[
                (covid_case['area'] == row['county']) &
                (covid_case['date'] <= row['End date']) &
                (covid_case['date'] >= row['Start date'])
            ]
            # Sum up the cases
            case_number = county_cases['cases'].sum()
        else:
            case_number = None

        case_numbers.append(case_number)

    return case_numbers

def calculate_county_deaths(weeklydata, covid_case):
    """
    Calculate the deaths number for other types (not prison).
    """
    # Convert date columns to datetime objects for comparison
    covid_case['date'] = pd.to_datetime(covid_case['date'])

    # Initialize an empty list to store deaths numbers
    deaths_numbers = []

    for index, row in weeklydata.iterrows():
        if row['Type'] != 'Prison':
            # Filter covid case data for the specific county and dates
            county_cases = covid_case[
                (covid_case['area'] == row['county']) &
                (covid_case['date'] <= row['End date']) &
                (covid_case['date'] >= row['Start date'])
            ]
            # Sum up the deaths
            deaths_number = county_cases['deaths'].sum()
        else:
            deaths_number = None

        deaths_numbers.append(deaths_number)

    return deaths_numbers

def main():
    # Load data
    file_path_weeklydata = 'weeklydata.csv' # Replace with your file path for weekly data
    file_path_prison_covid_cases = 'Prison covid cases.csv' # Replace with your file path for prison covid cases
    file_path_covid_case = 'covid case.csv' # Replace with your file path for county covid cases

    weeklydata = pd.read_csv(file_path_weeklydata)
    prison_covid_cases = pd.read_csv(file_path_prison_covid_cases)
    covid_case = pd.read_csv(file_path_covid_case)

    # Calculate case &deaths numbers for prison and other types
    prison_case_numbers = calculate_prison_cases(weeklydata, prison_covid_cases)
    county_case_numbers = calculate_county_cases(weeklydata, covid_case)
    prison_deaths_numbers = calculate_prison_death(weeklydata, prison_covid_cases)
    county_deaths_numbers = calculate_county_deaths(weeklydata, covid_case)

    # Assign the calculated case numbers to the weeklydata DataFrame
    weeklydata['case number'] = [p if p is not None else c for p, c in zip(prison_case_numbers, county_case_numbers)]
    weeklydata['deaths number'] = [p if p is not None else c for p, c in zip(prison_deaths_numbers, county_deaths_numbers)]

    # Save the updated data to a new CSV file
    weeklydata.to_csv('weeklydata.csv', index=False)
    print("Updated weekly data with case numbers saved to weeklydata.csv")

if __name__ == "__main__":
    main()
