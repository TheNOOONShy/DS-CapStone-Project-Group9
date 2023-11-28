import os
import re
import csv
import nltk
from nltk.corpus import stopwords
from flair.models import TextClassifier
from flair.data import Sentence

# stop word
stop_words = set(stopwords.words('english'))

# custom stop words
custom_stop_words = {"im","would","ive","could","us","one","know","going","thats","every","<br></br>","pm","[unintelligible]","dont","theyre","didnt","</br>","theres","…","___","”","youre","okay"}

stop_words = stop_words.union(custom_stop_words)

# load flair
classifier = TextClassifier.load('en-sentiment')

def get_sentiment(text):
    # not non
    if text.strip():
        sentence = Sentence(text)
        classifier.predict(sentence)
        # at less 1 lable
        if sentence.labels:
            label = sentence.labels[0]
            return label.value  # return POSITIVE or NEGATIVE
    return "NEUTRAL"  # if non return newtral


def clean_text(text):

    #to skip line
    text = text.replace('</br></br>', '\n').strip()
    lines = text.split('\n')
    clean_lines = [line for line in lines[1:] if not re.match(r'^(UCI:|uci:)', line, re.IGNORECASE)]
    # skip "Caller:"and "caller:" 
    clean_lines = [re.sub(r'[?.,;–!\’\"\'\“\‘\”%():-]', '', re.sub(r'^(Caller:|caller:)', '', line, flags=re.IGNORECASE).strip()) for line in clean_lines if line]
    return '\n'.join(clean_lines)


folder_path = '/Users/youli/Desktop/UC_Irvine/FQ_2023/DS-CapStone-Project-Group9/sponsor_data/data txt and docx/'


total_positives = {}
total_negatives = {}

for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        print(f"Processing {file_name}...")  
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            file_content = file.read().lower()
            if not file_content.strip(): 
                print(f"Skipping empty file {file_name}.")
                continue  # 跳过空文件

            cleaned_file_content = clean_text(file_content)  
            words = cleaned_file_content.split()  # split to word
            unique_words = set(word for word in words if word not in stop_words)  
            
            sentiment = get_sentiment(cleaned_file_content)  

            for word in unique_words:
                if sentiment == 'POSITIVE':
                    total_positives[word] = total_positives.get(word, 0) + 1
                elif sentiment == 'NEGATIVE':
                    total_negatives[word] = total_negatives.get(word, 0) + 1


output_csv_path = '/Users/youli/Desktop/word_counts.csv'
with open(output_csv_path, 'w', newline='') as csvfile:
    fieldnames = ['word', 'positive_count', 'negative_count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for word in set(total_positives.keys()) | set(total_negatives.keys()):  # 并集所有单词
        writer.writerow({
            'word': word,
            'positive_count': total_positives.get(word, 0),
            'negative_count': total_negatives.get(word, 0)
        })

print(f"CSV file has been created at {output_csv_path}.")