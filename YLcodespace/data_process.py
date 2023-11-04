import csv
import pandas as pd

def count(filename, column_name):
    unique_elements = set()
    with open(filename, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            unique_elements.add(row[column_name])
    return unique_elements

def rows(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        row_count = sum(1 for row in reader)
    print(f'The file has {row_count} rows.')

#outfilename need be like "xxx.csv"
def polaritychange(infilename,outfilename):
    

    # Load the CSV file
    data = pd.read_csv(filename)

    # Apply the transformation to the Polarity column
    data['Polarity'] = data.apply(
        lambda row: 1 - row['Polarity'] if row['Sentiment'] == 'NEGATIVE' else row['Polarity'],
        axis=1
    )

    # Save the transformed data to a new CSV file
    transformed_file_path = outfilename
    data.to_csv(transformed_file_path, index=False)
