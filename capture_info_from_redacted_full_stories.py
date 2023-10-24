import csv

full_information = []
fields = ['file_name', 'date', 'prison_name', 'tags']

with open('data/Redacted Full Stories - MDS Capstone.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line = 0
    for row in csv_reader:
        if line == 0: 
            line+=1
            continue
        information = []
        story_id = row[0]
        file_name = story_id
        index_for_date = story_id.find("2")
        prison_name = story_id[0:index_for_date-1]
        date = story_id[index_for_date:index_for_date+8]
        tags = row[12].split(",")
        if len(tags) == 0:
            tags = ""
        information = [file_name, date, prison_name, tags]
        full_information.append(information)

filename = "data/redacted_full_stories_table.csv"
    
with open(filename, 'w') as csvfile:  
    csvwriter = csv.writer(csvfile)     
    csvwriter.writerow(fields)  
    csvwriter.writerows(full_information) 
