import pandas as pd
import os
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import mammoth

# Initialize the sentiment analyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Directory containing the text and docx files
data_dir = "data txt and docx"
output_file = "sentiment_analysis_results.csv"

# Create empty lists to store the results
file_names = []
neg_sentiment = []
neu_sentiment = []
pos_sentiment = []
compound_sentiment = []

# Function to extract text from docx files using mammoth
def extract_text_from_docx(docx_file):
    with open(docx_file, "rb") as file:
        result = mammoth.extract_raw_text(file)
        return result.value

# Function to split text into lines using "</br></br>" as a delimiter
def split_text_into_lines(text):
    lines = text.split("</br></br>")
    return [line.strip() for line in lines if line.strip()]

# Iterate through files in the directory
for filename in os.listdir(data_dir):
    if filename.endswith(".txt"):
        with open(os.path.join(data_dir, filename), "r", errors="replace") as file:
            text = file.read()
    elif filename.endswith(".docx"):
        text = extract_text_from_docx(os.path.join(data_dir, filename))
    else:
        continue

    print(f'running {filename}')

    # For files with "UCI" and "Caller" lines, extract only the "Caller" lines
    text = re.sub(r"UCI:.*?Caller:", "", text)

    # Split the text into lines
    lines = split_text_into_lines(text)

    # Calculate sentiment scores using VADER
    sentiment = sia.polarity_scores(text)

    # Calculate sentiment scores using TextBlob
    tb = TextBlob(text)
    tb_sentiment = tb.sentiment

    # Append results to the lists
    file_names.append(filename)
    neg_sentiment.append(sentiment['neg'])
    neu_sentiment.append(sentiment['neu'])
    pos_sentiment.append(sentiment['pos'])
    compound_sentiment.append(sentiment['compound'])

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
