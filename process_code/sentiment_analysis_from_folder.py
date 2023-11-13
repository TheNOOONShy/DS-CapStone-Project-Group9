import pandas as pd
import os
import re
import nltk
import csv
import mammoth
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
from textblob import TextBlob

# Initialize the sentiment analyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Directory containing the text and docx files
sponsor_dir = "sponsor_data"
data_dir = "data txt and docx"
output_file = "Sentiment_Result/sentiment_analysis_results.csv"
output_file_breakdown = "Sentiment_Result/sentiment_analysis_results_breakdown.csv"

# Create empty lists to store the results
file_names = []
neg_sentiment = []
neu_sentiment = []
pos_sentiment = []
compound_sentiment = []
file_name_list = []
sentiment_analysis_map = dict()
sentiment_analysis_overall_map = dict()
neg_sentiment_map = dict()
neu_sentiment_map = dict()
pos_sentiment_map = dict()

class SentimentAnalysis:
  def __init__(self, neg, pos, neu, compound):
    self.neg = neg
    self.pos = pos
    self.neu = neu
    self.compound = compound

def remove(text, eliminated_char):
    return str(np.char.replace(text, eliminated_char, ''))

# Function to extract text from docx files using mammoth
def extract_text_from_docx(docx_file):
    with open(docx_file, "rb") as file:
        result = mammoth.extract_raw_text(file)
        return result.value

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
            with open(os.path.join(sponsor_dir, data_dir, filename), "r", errors="replace") as file:
                text = file.read()
        elif filename.endswith(".docx"):
            text = extract_text_from_docx(os.path.join(sponsor_dir, data_dir, filename))
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

        # Calculate sentiment scores using VADER
        sentiment = sia.polarity_scores(text_for_sentiment)

        # Calculate sentiment scores using TextBlob
        tb = TextBlob(text)
        tb_sentiment = tb.sentiment

        # Append results to the lists
        file_names.append(filename)
        neg_sentiment.append(sentiment['neg'])
        neu_sentiment.append(sentiment['neu'])
        pos_sentiment.append(sentiment['pos'])
        compound_sentiment.append(sentiment['compound'])

        if breakdown_sentence:
            sentiment_analysis_overall_map[filename] = SentimentAnalysis(
                sentiment['neg'], sentiment['pos'], sentiment['neu'], sentiment['compound'])
            
            sentences = sent_tokenize(text_for_sentiment)
            overall_result = categorized_compound_score(sentiment['compound'])

            neg_sentiment_temp = []
            neu_sentiment_temp = []
            pos_sentiment_temp = []

            for sentence in sentences:
                if "UCI:" in sentence:
                    continue
                sentiment_1 = sia.polarity_scores(sentence)
                sentence_result = categorized_compound_score(sentiment_1['compound'])

                if overall_result == 1:
                    if sentence_result == 0:
                        neu_sentiment_temp.append(sentence)
                    elif sentence_result == -1:
                        neg_sentiment_temp.append(sentence)
                elif overall_result == -1:
                    if sentence_result == 1:
                        pos_sentiment_temp.append(sentence)
                    elif sentence_result == 0:
                        neu_sentiment_temp.append(sentence)
                else:
                    if sentence_result == 1:
                        pos_sentiment_temp.append(sentence)
                    elif sentence_result == -1:
                        neg_sentiment_temp.append(sentence)
                
                if filename not in sentiment_analysis_map:
                    sentiment_analysis_map[filename] = []
                sentiment_analysis_map[filename].append(
                    SentimentAnalysis(sentiment_1['neg'], sentiment_1['pos'], sentiment_1['neu'], sentiment_1['compound']))

            neg_sentiment_map[filename] = neg_sentiment_temp
            neu_sentiment_map[filename] = neu_sentiment_temp
            pos_sentiment_map[filename] = pos_sentiment_temp

                
def categorized_compound_score(score):
    if score >= 0.05:
        return 1
    elif score <= -0.05:
        return -1
    else:
        return 0


def write_to_csv_with_pd():
    # Create a pandas DataFrame from the results
    data = {
        'Filename': file_names,
        'Negative Sentiment': neg_sentiment,
        'Neutral Sentiment': neu_sentiment,
        'Positive Sentiment': pos_sentiment,
        'Compound Sentiment': compound_sentiment
    }
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv(output_file, index=False)

    print("Sentiment analysis results saved to", output_file)

def collect_data_to_row():
    results = []
    fields = ["filename", "overall_result", "overall_compound_score", "compound_score", 
              "avg_compound", "negative_sentences", "positive_sentences", "neutral_sentences"]
    for filename in file_name_list:
        total = 0
        compound_score_list = []
        for sentiment in sentiment_analysis_map[filename]:
            compound_score_list.append(sentiment.compound)
            total += sentiment.compound
        average = total/len(sentiment_analysis_map[filename])
        result = [filename, 
                  categorized_compound_score(sentiment_analysis_overall_map[filename].compound), 
                  sentiment_analysis_overall_map[filename].compound, 
                  compound_score_list, average, 
                  neg_sentiment_map[filename],
                  pos_sentiment_map[filename],
                  neu_sentiment_map[filename]]
        results.append(result)
    return results, fields


def write_to_csv(fields, results):
    with open(output_file_breakdown, 'w') as csvfile:  
        csvwriter = csv.writer(csvfile)     
        csvwriter.writerow(fields)  
        csvwriter.writerows(results) 
    print("Sentiment analysis results saved to", output_file_breakdown)


if __name__ == "__main__":
    breakdown = True
    read_and_collect_data(breakdown)
    if breakdown:
        results, fields = collect_data_to_row()
        write_to_csv(fields, results)
    else:
        write_to_csv_with_pd()
