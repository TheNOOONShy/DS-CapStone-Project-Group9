import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import requests
import re

# Download the NLTK VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

# Load the CSV file with the correct file path
csv_file = "Data CSV's/Redacted Full Stories - MDS Capstone.csv"
data = pd.read_csv(csv_file)

# Initialize the Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

# Create an empty dictionary to store sentiment analysis values for each story
sentiment_dict = {}

# Iterate through the rows of the CSV file
for index, row in data.iterrows():
    story_id = row["Story ID (prison_yyyymmdd_topic)"]
    dropbox_link = row["Transcript"]
    print(f'Running {story_id}')
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
                            sentiment = sia.polarity_scores(caller_sentiment_text)
                            story_sentiments.append(sentiment)
                    elif "UCI:" not in paragraph:
                        # Perform sentiment analysis on the paragraph
                        sentiment = sia.polarity_scores(paragraph)
                        story_sentiments.append(sentiment)

                # Store the list of sentiment analysis values in the dictionary
                sentiment_dict[story_id] = story_sentiments
                print(story_sentiments)
        except Exception as e:
            print(f"Error processing Dropbox link for Story ID {story_id}: {str(e)}")

# Print the sentiment dictionary
for story_id, sentiment_values in sentiment_dict.items():
    print("Story ID:", story_id)
    for i, sentiment in enumerate(sentiment_values):
        print(f"Paragraph {i + 1} Sentiment Scores:", sentiment)
    print()
