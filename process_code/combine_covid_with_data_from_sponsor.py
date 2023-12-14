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
    start_date = end_date + datetime.timedelta(days=1)
    if end_date.year == 2024:
        stop = True

confirmed_cases_dict = dict()
temp_dictionary = dict()
with open('data/new_Covid_CA_2020_Weekly_stats.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line = 0
    for row in csv_reader:
        if line == 0 or line == 2:
            line+=1
            continue
        if line == 1:
            number = 1
            for single_box in row:
                if single_box != '' and single_box[0] == '2':
                    date = single_box.split(" ")[0]
                    date_split = date.split("/")
                    year = date_split[0]
                    month = date_split[1]
                    day = date_split[2]
                    date_datetime_format = datetime.datetime(int(year), int(month), int(day))
                    confirmed_cases_dict[date_datetime_format] = dict()
                    temp_dictionary[number] = date_datetime_format
                    number+=1
            line+=1
            continue
        prison_name = row[0]
        for i in range(1, len(row)-1):
            date = temp_dictionary[i]
            dictionary = confirmed_cases_dict[date]
            dictionary[prison_name] = row[i]

with open('data/new_Covid_CA_2021_Weekly_stats.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line = 0
    for row in csv_reader:
        if line == 0 or line == 2:
            line+=1
            continue
        if line == 1:
            number = 1
            for single_box in row:
                if single_box != '' and single_box[0] == '2':
                    date = single_box.split(" ")[0]
                    date_split = date.split("/")
                    year = date_split[0]
                    month = date_split[1]
                    day = date_split[2]
                    date_datetime_format = datetime.datetime(int(year), int(month), int(day))
                    confirmed_cases_dict[date_datetime_format] = dict()
                    temp_dictionary[number] = date_datetime_format
                    number+=1
            line+=1
            continue
        prison_name = row[0]
        for i in range(1, len(row)-1):
            date = temp_dictionary[i]
            dictionary = confirmed_cases_dict[date]
            dictionary[prison_name] = row[i]

with open('data/new_Covid_CA_2022_Weekly_stats.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line = 0
    for row in csv_reader:
        if line == 0 or line == 2:
            line+=1
            continue
        if line == 1:
            number = 1
            for single_box in row:
                if single_box != '' and single_box[0] == '2':
                    date = single_box.split(" ")[0]
                    date_split = date.split("/")
                    year = date_split[0]
                    month = date_split[1]
                    day = date_split[2]
                    date_datetime_format = datetime.datetime(int(year), int(month), int(day))
                    confirmed_cases_dict[date_datetime_format] = dict()
                    temp_dictionary[number] = date_datetime_format
                    number+=1
            line+=1
            continue
        prison_name = row[0]
        for i in range(1, len(row)-1):
            date = temp_dictionary[i]
            dictionary = confirmed_cases_dict[date]
            dictionary[prison_name] = row[i]

with open('data/new_Covid_CA_2023_Weekly_stats.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line = 0
    for row in csv_reader:
        if line == 0 or line == 2:
            line+=1
            continue
        if line == 1:
            number = 1
            for single_box in row:
                if single_box != '' and single_box[0] == '2':
                    date = single_box.split(" ")[0]
                    date_split = date.split("/")
                    year = date_split[0]
                    month = date_split[1]
                    day = date_split[2]
                    date_datetime_format = datetime.datetime(int(year), int(month), int(day))
                    confirmed_cases_dict[date_datetime_format] = dict()
                    temp_dictionary[number] = date_datetime_format
                    number+=1
            line+=1
            continue
        prison_name = row[0]
        for i in range(1, len(row)-1):
            date = temp_dictionary[i]
            dictionary = confirmed_cases_dict[date]
            dictionary[prison_name] = row[i]

print(confirmed_cases_dict)

full_information = []
fields = ['file_name', 'date', 'prison_name', 'tags', 'confirmed_cases', 'start_date', 'end_date']
with open('data/new_redacted_full_stories_table.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line = 0
    for row in csv_reader:
        if line == 0:
            line+=1
            continue
        file_name = row[1]
        date = row[2]
        year = date[0:4]
        month = date[4:6]
        day = date[6:]
        date_datetime_format = datetime.datetime(int(year), int(month), int(day))
        prison = row[0]
        tags = row[3]
        date_range = definition_of_week.get(date_datetime_format)
        start_date = date_range[0]
        end_date = date_range[1]
        dict_of_comfired_case = confirmed_cases_dict[start_date]
        information = [file_name, date, prison, tags, dict_of_comfired_case.get(prison, None), start_date, end_date]
        full_information.append(information)


filename = "data/combined_covid_script_final_table_weekly.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(full_information)
