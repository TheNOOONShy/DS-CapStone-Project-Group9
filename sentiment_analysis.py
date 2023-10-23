import pandas as pd
import requests
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import spacy
# from spacytextblob import TextBlob

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

def process_csv_sentiment_analysis(csv_file, sentiment_analyzer="nltk"):
    # Load the CSV file with the correct file path
    data = pd.read_csv(csv_file)

    # Create an empty dictionary to store sentiment analysis values for each story
    sentiment_dict = {}

    # Iterate through the rows of the CSV file
    for index, row in data.iterrows():
        story_id = row["Story ID (prison_yyyymmdd_topic)"]
        dropbox_link = row["Transcript"]
        print(f'\tRunning {story_id}')
        if not pd.isnull(dropbox_link):  # Check for missing values in the Dropbox link
            # Assuming the Dropbox links point to plain text files (e.g., .txt files)
            try:
                if "www.dropbox.com/s/" in dropbox_link:
                    # Replace "www.dropbox.com" with "dl.dropboxusercontent.com" to get the direct file URL
                    file_url = dropbox_link.replace("www.dropbox.com", "dl.dropboxusercontent.com")

                    response = requests.get(file_url, allow_redirects=True)
                    text_content = response.text

                    # Remove "</br></br>" tags from the text content
                    text_content = text_content.replace("</br></br>", "")

                    # Split the text content into paragraphs using both "\n" and "\r"
                    paragraphs = re.split(r'[\n\r]+', text_content)

                    # Initialize a list to store sentiment analysis values for this story
                    story_sentiments = []

                    for i, paragraph in enumerate(paragraphs):
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

                    # Store the list of sentiment analysis values in the dictionary
                    sentiment_dict[story_id] = story_sentiments
            except Exception as e:
                print(f"Error processing Dropbox link for Story ID {story_id}: {str(e)}")

    # Save the sentiment dictionary to a CSV file
    sentiment_df = pd.DataFrame.from_dict(sentiment_dict, orient='index', columns=[f"Paragraph_{i + 1}" for i in range(len(story_sentiments))])
    sentiment_df.to_csv(f"sentiment_results_{sentiment_analyzer}.csv")

if __name__ == "__main__":
    csv_file = "Data CSV's/Redacted Full Stories - MDS Capstone.csv"
    sentiment_analyzers = ["nltk", "spacy"]

    for analyzer in sentiment_analyzers:
        print(f'running {analyzer}')
        process_csv_sentiment_analysis(csv_file, sentiment_analyzer=analyzer)
