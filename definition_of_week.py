import datetime
import csv

stop = False
definition_of_week = []
fields = ['start_date', 'end_date']
start_date = datetime.datetime(2020, 1, 1)

while(stop != True):
    end_date = start_date + datetime.timedelta(days=7)
    definition_of_week.append([start_date, end_date])
    start_date = end_date + + datetime.timedelta(days=1)
    if end_date.year == 2024:
        stop = True

filename = "data/definition_of_week.csv"
    
with open(filename, 'w') as csvfile:  
    csvwriter = csv.writer(csvfile)     
    csvwriter.writerow(fields)  
    csvwriter.writerows(definition_of_week) 
