import csv
import datetime

stop = False
definition_of_week = dict()
fields = ['start_date', 'end_date']
start_date = datetime.datetime(2020, 1, 1)

while(stop != True):
    end_date = start_date + datetime.timedelta(days=7)
    date = start_date
    for i in range(8):
        definition_of_week[date] = [start_date, end_date]
        date = date + datetime.timedelta(days=1)
    start_date = end_date + + datetime.timedelta(days=1)
    if end_date.year == 2024:
        stop = True


new_field = ['Date','InstitutionName','Latitude','Longitude','TotalConfirmed','TotalDeaths','DistinctPatientsTested','NewInTheLast14Days', 'StartDate', 'EndDate']
new_data = []
with open('data/Covid_CA_2023 - 2023.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line = 0
    for row in csv_reader:
        if line == 0: 
            line+=1
            continue
        date = row[0]
        date_split = date.split("/")
        month = date_split[0]
        day = date_split[1]
        year = date_split[2]
        date_datetime_format = datetime.datetime(int(year), int(month), int(day))
        date_range = definition_of_week.get(date_datetime_format)
        row.append(date_range[0])
        row.append(date_range[1])
        new_data.append(row)

filename = "data/Covid_CA_2023_Weekly.csv"
    
with open(filename, 'w') as csvfile:  
    csvwriter = csv.writer(csvfile)     
    csvwriter.writerow(new_field)  
    csvwriter.writerows(new_data) 
