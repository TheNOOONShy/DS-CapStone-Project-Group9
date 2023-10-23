import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import requests

# Download the NLTK VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

# Load the CSV file with the correct file path
csv_file = "Data CSV's/Redacted Full Stories - MDS Capstone.csv"
data = pd.read_csv(csv_file)

# Initialize the Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

# Create an empty list to store data for the DataFrame
result_data = []

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

                # Split the text content into paragraphs
                paragraphs = text_content.split('\n')
                print(paragraphs)
                for i, paragraph in enumerate(paragraphs):
                    if "UCI:" not in paragraph:  # Check if "UCI:" is not in the paragraph
                        # Perform sentiment analysis on the cleaned paragraph
                        sentiment = sia.polarity_scores(paragraph)
                        result_data.append({
                            "Story ID": story_id,
                            "Paragraph Number": i + 1,
                            "Sentiment Scores": sentiment,
                            "Dropbox Link": dropbox_link
                        })
        except Exception as e:
            print(f"Error processing Dropbox link for Story ID {story_id}: {str(e)}")

# Create a Pandas DataFrame from the result_data list
df = pd.DataFrame(result_data)

# Save the DataFrame to a CSV file
output_csv = "sentiment_analysis_results.csv"
df.to_csv(output_csv, index=False)
