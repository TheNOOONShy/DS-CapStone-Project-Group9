import pandas as pd
import os
import re
import flair
import flair.models
from flair.data import Sentence
import mammoth

# Initialize Flair sentiment model
flair_sentiment_model = flair.models.TextClassifier.load('sentiment')

# Directory containing the text and docx files
data_dir = "data txt and docx"
output_file = "sentiment_analysis_results_flair.csv"

# Create empty lists to store the results
file_names = []
sentiments = []

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
    lines = text.split("</br></br>")
    return [line.strip() for line in lines if line.strip()]

# Iterate through files in the directory
for filename in os.listdir(data_dir):
    if filename.endswith(".txt"):
        with open(os.path.join(data_dir, filename), "r", encoding="utf-8", errors="replace") as file:
            text = remove_undecodable_bytes(file.read())
    elif filename.endswith(".docx"):
        text = extract_text_from_docx(os.path.join(data_dir, filename))
        text = remove_undecodable_bytes(text)
    else:
        continue

    print(f'running {filename}')

    # For files with "UCI" and "Caller" lines, extract only the "Caller" lines
    text = re.sub(r"UCI:.*?Caller:", "", text)

    # Split the text into lines
    lines = split_text_into_lines(text)

    # Combine lines into a single string for sentiment analysis
    text_for_sentiment = " ".join(lines)

    # Create a Flair Sentence for sentiment analysis
    sentence = Sentence(text_for_sentiment)

    # Predict sentiment using the Flair model
    flair_sentiment_model.predict(sentence)
    sentiment_label = sentence.labels[0].value

    # Append results to the list
    file_names.append(filename)
    sentiments.append(sentiment_label)

# Create a pandas DataFrame from the results
data = {
    'Filename': file_names,
    'Sentiment': sentiments
}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv(output_file, index=False)

print("Sentiment analysis results saved to", output_file)
