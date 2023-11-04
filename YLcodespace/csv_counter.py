import csv

def count(filename, column_name):
    unique_elements = set()
    with open(filename, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            unique_elements.add(row[column_name])
    return unique_elements

if __name__ == "__main__":
    filename = 'merged3files.csv'
    column_name = 'prison_name'
    unique_elements = count(filename, column_name)
    print(unique_elements)
