
import csv


file_path = '/Users/youli/Desktop/UC_Irvine/FQ_2023/DS-CapStone-Project-Group9/Analysis CSVs/merged3files.csv'


with open(file_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    row_count = sum(1 for row in reader)

print(f'The file has {row_count} rows.')