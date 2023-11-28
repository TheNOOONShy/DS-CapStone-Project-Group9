import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

import pandas as pd
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize

# Function to get the part of speech for a word
def get_pos(word):
    # Ensure the word is a string
    word = str(word)
    tokens = word_tokenize(word)
    pos = pos_tag(tokens)
    return pos[0][1] if pos else None


# Read the CSV file
file_path = '/Users/youli/Desktop/word_counts.csv'  # Replace with your file path
word_counts_df = pd.read_csv(file_path)

# Apply the function to the 'word' column
word_counts_df['part_of_speech'] = word_counts_df['word'].apply(get_pos)

# Save the updated dataframe to a new CSV file
updated_file_path = '/Users/youli/Desktop/word_counts.csv'  # Replace with your desired path
word_counts_df.to_csv(updated_file_path, index=False)

print("File updated with part of speech and saved to", updated_file_path)
