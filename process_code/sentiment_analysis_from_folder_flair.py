import pandas as pd
import os
import re
import flair
import flair.models
import numpy as np
import mammoth
import csv
from flair.data import Sentence
from nltk.tokenize import sent_tokenize

# import nltk
# import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# nltk.download()

# Initialize Flair sentiment model
flair_sentiment_model = flair.models.TextClassifier.load('sentiment')

# Directory containing the text and docx files
sponsor_dir = "sponsor_data"
data_dir = "data txt and docx"
output_file = "Sentiment_Result/sentiment_analysis_results_flair.csv"
output_file_breakdown = "Sentiment_Result/sentiment_analysis_results_breakdown_flair.csv"

# Create empty lists to store the results
file_names = []
sentiments = []
polarity_values = []
score_map = dict()
sentiment_label_map = dict()
file_name_list = []
positive_sentences_map = dict()
negative_sentences_map = dict()

class SentimentAnalysis:
  def __init__(self, label, polarity):
    self.label = label
    self.polarity = polarity
 
def remove(text, eliminated_char):
    return str(np.char.replace(text, eliminated_char, ''))

# Function to extract text from docx files using mammoth
def extract_text_from_docx(docx_file):
    with open(docx_file, "rb") as file:
        result = mammoth.extract_raw_text(file)
        return result.value

# Function to remove undecodable bytes from text
def remove_undecodable_bytes(text):
    return text.encode('ascii', 'replace').decode('ascii')

# Function to split text into lines using "</br></br>" as a delimiter
def split_text_into_lines(text):
    text = remove(text, "<em>")
    text = remove(text, "</em>\n\n")
    lines = text.split("</br></br>")
    return [line.strip() for line in lines if line.strip()]


def read_and_collect_data(breakdown_sentence):
    # Iterate through files in the directory
    for filename in os.listdir(os.path.join(sponsor_dir, data_dir)):
        if filename.endswith(".txt"):
            with open(os.path.join(sponsor_dir, data_dir, filename), 
                      "r", encoding="utf-8", errors="replace") as file:
                text = remove_undecodable_bytes(file.read())
        elif filename.endswith(".docx"):
            text = extract_text_from_docx(os.path.join(sponsor_dir, data_dir, filename))
            text = remove_undecodable_bytes(text)
        else:
            continue

        print(f'running {filename}')
        file_name_list.append(filename)

        # For files with "UCI" and "Caller" lines, extract only the "Caller" lines
        text = re.sub(r"UCI:.*?Caller:", "", text)

        # Split the text into lines
        lines = split_text_into_lines(text)

        # Combine lines into a single string for sentiment analysis
        text_for_sentiment = " ".join(lines)

        sentence = Sentence(text_for_sentiment)
        flair_sentiment_model.predict(sentence)
        sentiment_label_overall = sentence.labels[0].value
        polarity_overall = sentence.labels[0].score

        # Append results to the list
        file_names.append(filename)
        sentiments.append(sentiment_label_overall)
        polarity_values.append(polarity_overall)  # Append polarity value

        positive_sentences = []
        negative_sentences = []

        if breakdown_sentence:
            sentiment_label_map[filename] = SentimentAnalysis(sentiment_label_overall, polarity_overall)

            sentences = sent_tokenize(text_for_sentiment)

            for sentence in sentences:
                if "UCI:" in sentence:
                    continue
                sentence = Sentence(sentence)
                flair_sentiment_model.predict(sentence)
                sentiment_label = sentence.labels[0].value
                polarity = sentence.labels[0].score

                if sentiment_label_overall=='NEGATIVE':
                    if sentiment_label=='NEGATIVE':
                        polarity = -(sentence.labels[0].score)
                    else:
                        positive_sentences.append(sentence)
                else:
                    if sentiment_label=='NEGATIVE':
                        polarity = -(sentence.labels[0].score)
                        negative_sentences.append(sentence)

                if filename not in score_map:
                    score_map[filename] = []
                score_map[filename].append(SentimentAnalysis(sentiment_label, polarity))

        negative_sentences_map[filename] = negative_sentences
        positive_sentences_map[filename] = positive_sentences


def write_to_csv(fields, results):
    with open(output_file_breakdown, 'w') as csvfile:  
        csvwriter = csv.writer(csvfile)     
        csvwriter.writerow(fields)  
        csvwriter.writerows(results) 
    print("Sentiment analysis results saved to", output_file_breakdown)


def write_to_csv_with_pd():
    # # Create a pandas DataFrame from the results
    data = {
        'Filename': file_names,
        'Sentiment': sentiments,
        'Polarity': polarity_values  # Add polarity values to the DataFrame
    }
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv(output_file, index=False)
    print("Sentiment analysis results saved to", output_file)


def collect_data_to_row():
    results = []
    fields = ["filename", "overall_label", "overall_polarity", "sentimental_label_list", "sentimental_polarity_list", 
              "avg_polarity", "negative_sentences", "positive_sentences"]
    for filename in file_name_list:
        total = 0
        polarity_list = []
        label_list = []
        for sentiment in score_map[filename]:
            polarity_list.append(sentiment.polarity)
            label_list.append(sentiment.label)
            total += sentiment.polarity
        average = total/len(score_map[filename])
        result = [filename, sentiment_label_map[filename].label, sentiment_label_map[filename].polarity, 
                  label_list, polarity_list, average, negative_sentences_map[filename], positive_sentences_map[filename]]
        results.append(result)
    return results, fields


if __name__ == "__main__":
    breakdown = True
    read_and_collect_data(breakdown)
    if breakdown:
        results, fields = collect_data_to_row()
        write_to_csv(fields, results)
    else:
        write_to_csv_with_pd()
