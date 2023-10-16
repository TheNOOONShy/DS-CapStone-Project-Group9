import csv
import requests

# CSV file containing the Dropbox file links
csv_file = "Redacted Full Stories - MDS Capstone.csv"
column_name = "Transcript"

readable_count = 0
unreadable_count = 0
unreadable_stories = []

# Open the CSV file and iterate through the rows
with open(csv_file, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        if column_name in row:
            dropbox_link = row[column_name]

            # Ensure that the link is a public Dropbox file link
            if "www.dropbox.com/s/" in dropbox_link:
                # Check if the file is readable
                response = requests.head(dropbox_link)
                if response.status_code == 200:
                    readable_count += 1
                else:
                    unreadable_count += 1
                    # Store the content from the "Story ID (prison_yyyymmdd_topic)" column for unreadable stories
                    story_id = row.get("Story ID (prison_yyyymmdd_topic)")
                    if story_id:
                        unreadable_stories.append(story_id)

# List the unreadable stories and provide total counts
print(f"Total readable files: {readable_count}")
print(f"Total unreadable files: {unreadable_count}")
print("Unreadable Stories:")
for story in unreadable_stories:
    print(story)
