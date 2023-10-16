import csv
import requests

# CSV file containing the Dropbox file links
csv_file = "Redacted Full Stories - MDS Capstone.csv"
# The name of the column containing the Dropbox links
column_name = "Transcript"

readable_count = 0
unreadable_count = 0
unreadable_stories = []
interview_count = 0
story_count = 0

# Open the CSV file and iterate through the rows
with open(csv_file, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        if column_name in row:
            dropbox_link = row[column_name]

            # Ensure that the link is a public Dropbox file link
            if "www.dropbox.com/s/" in dropbox_link:
                # Check if the file is readable while following the redirection
                response = requests.head(dropbox_link, allow_redirects=True)
                status_code = response.status_code

                if status_code == 200:
                    readable_count += 1
                else:
                    unreadable_count += 1
                    # Store the content from the "Story ID (prison_yyyymmdd_topic)" column for unreadable stories
                    story_id = row.get("Story ID (prison_yyyymmdd_topic)")
                    if story_id:
                        unreadable_stories.append((story_id, status_code))

                # Check if the content looks like an interview
                transcript = row[column_name]
                if "Caller:" in transcript and "UCI:" in transcript:
                    interview_count += 1
                else:
                    story_count += 1

# List the unreadable stories and provide total counts with status codes
print(f"Total readable files: {readable_count}")
print(f"Total unreadable files: {unreadable_count}")
print("Unreadable Stories:")
for story_id, status_code in unreadable_stories:
    print(f"Story ID: {story_id}, Status Code: {status_code}")

# List the counts of interviews and stories
print(f"Total interview entries: {interview_count}")
print(f"Total story entries: {story_count}")
