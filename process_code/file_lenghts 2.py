import os
import csv
import mammoth

def custom_split(content):
    return content.replace("</br></br>", "\n").split("\n")

def process_file(file_path):
    print(f"Processing file: {file_path}")
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()

    if "UCI:" in content and "Caller:" in content:
        is_call = 1
        lines = custom_split(content)
        relevant_lines = [line for line in lines if "Caller:" in line]
        length = sum(len(line) for line in relevant_lines)
    else:
        is_call = 0
        length = len(content)

    return {
        'file_name': os.path.basename(file_path),
        'is_call': is_call,
        'length': length
    }

def process_docx(file_path):
    print(f"Processing docx: {file_path}")
    with open(file_path, 'rb') as file:
        result = mammoth.extract_raw_text(file)
        content = result.value.encode('utf-8', errors='replace').decode('utf-8')

    if "UCI:" in content and "Caller:" in content:
        is_call = 1
        lines = custom_split(content)
        relevant_lines = [line for line in lines if "Caller:" in line]
        length = sum(len(line) for line in relevant_lines)
    else:
        is_call = 0
        length = len(content)

    return {
        'file_name': os.path.basename(file_path),
        'is_call': is_call,
        'length': length
    }

def main():
    output_file = 'C:\\Users\\reada\\github\\DS-CapStone-Project-Group9\\output.csv'

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['file_name', 'is_call', 'length']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        base_folder = 'C:\\Users\\reada\\github\\DS-CapStone-Project-Group9\\data txt and docx'

        for filename in os.listdir(base_folder):
            file_path = os.path.join(base_folder, filename)

            if filename.endswith('.txt'):
                data = process_file(file_path)
            elif filename.endswith('.docx'):
                data = process_docx(file_path)
            else:
                continue

            print(f"Writing data: {data}")
            writer.writerow(data)

if __name__ == "__main__":
    main()
