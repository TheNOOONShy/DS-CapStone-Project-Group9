import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))


def remove_specific_words(text, words_to_remove):
    # Create a pattern that matches any of the words to remove
    pattern = r'\b(?:' + '|'.join(map(re.escape, words_to_remove)) + r')\b'
    # Replace the matched words with an empty string
    text = re.sub(pattern, '', text, flags=re.IGNORECASE)
    # Remove extra spaces left by word removals
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def remove_word_pattern(text, word):
    # Define a regex pattern to match the word in all cases
    # \b - word boundary (ensures we are matching whole words, not substrings within words)
    # (?i) - case insensitive matching
    pattern = r'\b(?i)' + re.escape(word) + r'\b'
    
    # Replace the pattern with an empty string
    modified_text = re.sub(pattern, '', text)

    # Return the modified text
    return modified_text

# Words to remove as provided by the user
words_to_remove = [
    'know', "got", "yeah", "people", "one", "really", "even", "guy", "nothing",
    "right", "mean", "say", "going", "little", "well", "still", "thing", "actually",
    "go", "see", "u", "okay", "phone", "whatever","us","time","think","want","s","always","now","that'","it'","start",
    "thing","guy","way","lot","one","re","day","come","they'","people","something","we'",
    "somebody","everything","give","put","Thank","number","let","two","given","done","back","need","Oh","oh","much","came",
    "ve","take","went","man","anything","already","first","many","everyone","there'","guys","I'",
    "three","m"
]


def extract_interview_text(filename, base_path):
    # Add .txt extension if not present
    if not filename.endswith('.txt'):
        filename += '.txt'
    
    try:
        with open(os.path.join(base_path, filename), 'r', encoding='utf-8') as file:
            text = file.read()
            # Remove <br> and </br> tags with variations
            text = re.sub(r'</?br\s*/?>', ' ', text, flags=re.IGNORECASE)
            # Remove lines containing "UCI:" and the word "Caller:" itself
            text = re.sub(r'^.*UCI:.*$', '', text, flags=re.MULTILINE)
            text = re.sub(r'Caller:', '', text, flags=re.MULTILINE)
            # Remove extra whitespace
            cleaned_text = re.sub(r'\s+', ' ', text).strip()
            # print(cleaned_text)
            cleaned_text = remove_specific_words(cleaned_text, words_to_remove)
            # Tokenize the text and remove stop words
            words = cleaned_text.split()
            cleaned_text = ' '.join(word for word in words if word.lower() not in stop_words)
            # pattern = r'[ ,\.\-\?]+'
            # words = re.split(pattern, cleaned_text)
            # # words = cleaned_text.split()
            # # words = cleaned_text.split(',')
            # cleaned_text = ' '.join(word for word in words if word.lower() not in words_to_remove)
            return cleaned_text
    except UnicodeDecodeError:
        try:
            with open(os.path.join(base_path, filename), 'r', encoding='latin1') as file:
                text = file.read()
                # Repeat the same cleanup and stop words removal
                text = re.sub(r'</?br\s*/?>', ' ', text, flags=re.IGNORECASE)
                text = re.sub(r'^.*UCI:.*$', '', text, flags=re.MULTILINE)
                text = re.sub(r'Caller:', '', text, flags=re.MULTILINE)

                cleaned_text = re.sub(r'\s+', ' ', text).strip()
                cleaned_text = remove_specific_words(cleaned_text, words_to_remove)
                words = cleaned_text.split()
                cleaned_text = ' '.join(word for word in words if word.lower() not in stop_words)
                # pattern = r'[ ,\.\-\?]+'
                # words = re.split(pattern, cleaned_text)
                # # words = cleaned_text.split()
                # # words = cleaned_text.split(',')
                # cleaned_text = ' '.join(word for word in words if word.lower() not in words_to_remove)
                return cleaned_text
        except UnicodeDecodeError as e:
            print(f"Error reading {filename} with 'latin1' encoding: {e}")
            return ""
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return ""


# Main function to process files and generate word cloud
def generate_word_cloud(csv_path, base_path):
    # Load the CSV to get the filenames
    csv_data = pd.read_csv(csv_path)

    # Read and extract text from all files listed in the CSV
    all_interview_texts = ""
    for filename in csv_data['Filename']:
        all_interview_texts += extract_interview_text(filename, base_path)
    print(all_interview_texts.split())
    # Check if any text was collected
    if not all_interview_texts.strip():
        raise ValueError("No text found. Please check your files and paths.")

    # Create a word cloud object
    wordcloud = WordCloud(width=800, height=800, background_color='white').generate(all_interview_texts)

    # Display the generated word cloud
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

# Set your CSV file path and the base path for your text files
csv_file_path = '/Users/youli/Desktop/UC_Irvine/FQ_2023/DS-CapStone-Project-Group9/Analysis CSVs/updated_7days.csv'
text_files_base_path = '/Users/youli/Desktop/UC_Irvine/FQ_2023/DS-CapStone-Project-Group9/data txt and docx'

# print(stop_words)
# Call the main function
generate_word_cloud(csv_file_path, text_files_base_path)
