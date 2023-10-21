import csv
import requests
import re

# CSV file containing the Dropbox file links
csv_file = "Redacted Full Stories - MDS Capstone.csv"
# The name of the column containing the Dropbox links
column_name = "Transcript"

readable_count = 0
unreadable_count = 0
unreadable_stories = []
interview_count = 0
story_count = 0
not_shared_count = 0
not_shared_files = []
non_alphanumeric_characters = set()  # Store non-alphanumeric characters in a set


# Function to check if the content of a file is an interview
def is_interview(content):
    return "Caller:" in content and "UCI:" in content

# Function to identify and store non-alphanumeric characters within the text
def identify_non_alphanumeric_characters(text):
    non_alphanumeric_chars = re.findall(r'[^A-Za-z0-9\s]', text)
    non_alphanumeric_characters.update(non_alphanumeric_chars)  # Add to the set

# Open the CSV file and iterate through the rows
with open(csv_file, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        if column_name in row:
            dropbox_link = row[column_name]

            # Check if the link is a Dropbox shared link
            if "www.dropbox.com/s/" in dropbox_link:
                # Check if the file is readable while following the redirection
                response = requests.head(dropbox_link, allow_redirects=True)
                status_code = response.status_code

                if status_code == 200:
                    readable_count += 1
                else:
                    unreadable_count += 1
                    story_id = row.get("Story ID (prison_yyyymmdd_topic)")
                    if story_id:
                        unreadable_stories.append((story_id, status_code))

                # Download the content of the file
                file_content = requests.get(dropbox_link).text

                # Check if the content looks like an interview
                if is_interview(file_content):
                    interview_count += 1
                else:
                    story_count += 1

                # Identify and store non-alphanumeric characters
                identify_non_alphanumeric_characters(file_content)
            else:
                not_shared_count += 1
                not_shared_files.append(row)

# List the unreadable stories and provide total counts with status codes
print(f"Total readable files: {readable_count}")
print(f"Total unreadable files: {unreadable_count}")
print("Unreadable Stories:")
for story_id, status_code in unreadable_stories:
    print(f"Story ID: {story_id}, Status Code: {status_code}")

# List the counts of interviews and stories
print(f"Total interview entries: {interview_count}")
print(f"Total story entries: {story_count}")

# List the count of files that aren't shared
print(f"Total files that aren't shared: {not_shared_count}")
print("Files that aren't shared:")
for file_info in not_shared_files:
    story_id = file_info.get("Story ID (prison_yyyymmdd_topic)")
    status_code = "N/A"
    print(f"Story ID: {story_id}, Status Code: {status_code}")

# Print the non-alphanumeric characters as a set
print("Non-Alphanumeric Characters:")
print(non_alphanumeric_characters)
