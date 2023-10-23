import pandas as pd
import requests
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import spacy

# Download the NLTK VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

def analyze_sentiment_nltk(paragraph, sentiment_analyzer):
    # Perform sentiment analysis using NLTK VADER or SpaCy
    if sentiment_analyzer == 'nltk':
        sia = SentimentIntensityAnalyzer()
        sentiment = sia.polarity_scores(paragraph)
    elif sentiment_analyzer == 'spacy':
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(paragraph)
        sentiment = {
            'polarity': doc._.polarity,
            'subjectivity': doc._.subjectivity
        }

    return sentiment

def get_sentiment_of_entire_file(text, sentiment_analyzer):
    if sentiment_analyzer == 'nltk':
        sia = SentimentIntensityAnalyzer()
        sentiment = sia.polarity_scores(text)
    elif sentiment_analyzer == 'spacy':
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        sentiment = {
            'polarity': doc._.polarity,
            'subjectivity': doc._.subjectivity
        }

    return sentiment

def process_csv_sentiment_analysis(csv_file, sentiment_analyzer="nltk", calculate_entire_file_sentiment=True):
    # Load the CSV file with the correct file path
    data = pd.read_csv(csv_file)

    # Create an empty list to store sentiment analysis results
    results = []

    # Iterate through the rows of the CSV file
    for index, row in data.iterrows():
        story_id = row["Story ID (prison_yyyymmdd_topic)"]
        dropbox_link = row["Transcript"]
        print(f'\tRunning {story_id}')
        if not pd.isnull(dropbox_link):  # Check for missing values in the Dropbox link
            # Check if the file is a text file (ending in .txt?dl=0)
            if dropbox_link.endswith('.txt?dl=0'):
                try:
                    # Replace "www.dropbox.com" with "dl.dropboxusercontent.com" to get the direct file URL
                    file_url = dropbox_link.replace("www.dropbox.com", "dl.dropboxusercontent.com")

                    response = requests.get(file_url, allow_redirects=True)
                    text_content = response.text

                    # Remove "</br></br>" tags from the text content
                    text_content = text_content.replace("</br></br>", "")

                    # Split the text content into paragraphs using both "\n" and "\r"
                    paragraphs = re.split(r'[\n\r]+', text_content)

                    # Initialize variables to store sentiment analysis values
                    story_sentiments = []
                    entire_file_sentiment = None

                    for paragraph in paragraphs:
                        if "UCI:" in paragraph:
                            # Check if "Caller:" is in the paragraph
                            if "Caller:" in paragraph:
                                # Extract text after "Caller:"
                                caller_sentiment_text = paragraph.split("Caller:", 1)[1].strip()
                                # Perform sentiment analysis on the caller sentiment text
                                sentiment = analyze_sentiment_nltk(caller_sentiment_text, sentiment_analyzer)
                                story_sentiments.append(sentiment)
                        elif "UCI:" not in paragraph:
                            # Perform sentiment analysis on the paragraph
                            sentiment = analyze_sentiment_nltk(paragraph, sentiment_analyzer)
                            story_sentiments.append(sentiment)

                    # Calculate sentiment of entire file content if enabled
                    if calculate_entire_file_sentiment:
                        entire_file_sentiment = get_sentiment_of_entire_file(text_content, sentiment_analyzer)

                    results.append({
                        "Story ID": story_id,
                        "Paragraph Sentiments": story_sentiments,
                        "Entire File Sentiment": entire_file_sentiment
                    })
                except Exception as e:
                    print(f"Error processing Dropbox link for Story ID {story_id}: {str(e)}")
            # Check if the file is an MP3 file (ending in .mp3?dl=0)
            elif dropbox_link.endswith('.mp3?dl=0'):
                print(f"Skipping MP3 file: {dropbox_link}")
            else:
                print(f"Skipping unknown file type: {dropbox_link}")

    # Create a DataFrame from the results
    df = pd.DataFrame(results)

    # Save the DataFrame to a CSV file
    df.to_csv(f"sentiment_results_{sentiment_analyzer}.csv", index=False)

if __name__ == "__main__":
    csv_file = "Data CSV's/Redacted Full Stories - MDS Capstone.csv"
    sentiment_analyzers = ["nltk",
                            # "spacy"
                            ]

    for analyzer in sentiment_analyzers:
        print(f'running {analyzer}')
        process_csv_sentiment_analysis(csv_file, sentiment_analyzer=analyzer, calculate_entire_file_sentiment=True)
