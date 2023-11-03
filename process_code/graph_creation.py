import pandas as pd
import matplotlib.pyplot as plt

def create_top_10_count_bar_graph(csv_file, column_name, title, head = 10):
    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(csv_file)

    # Count the occurrences of the specified column
    counts = data[column_name].value_counts().sort_values(ascending=False)

    # Select the top 10 items
    top_10 = counts.head(head)

    # Create a bar graph
    plt.figure(figsize=(10, 2*3))
    ax = top_10.plot(kind='bar')
    plt.title(title)
    plt.xlabel(column_name)
    plt.ylabel('Count')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

    # Annotate each bar with its count
    for i, count in enumerate(top_10):
        ax.text(i, count, str(count), ha='center', va='bottom')

    # Show the plot
    plt.tight_layout()
    plt.show()

def create_top_10_tags_bar_graph(csv_file, head = 10):
    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(csv_file)

    # Assuming the tags are in a column named "Tags" in the DataFrame
    tags = data["Tags"].str.split(', ').explode()  # Split and explode the tags

    # Count the occurrences of each tag
    tag_counts = tags.value_counts().sort_values(ascending=False)

    # Select the top 10 tags
    top_10_tags = tag_counts.head(head)

    # Create a bar graph
    plt.figure(figsize=(10, 6))
    top_10_tags.plot(kind='bar')
    plt.title('Top 10 Tags (Descending Order)')
    plt.xlabel('Tag')
    plt.ylabel('Count')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

    # Annotate each bar with its count
    ax = plt.gca()
    for i, count in enumerate(top_10_tags):
        ax.text(i, count, str(count), ha='center', va='bottom')

    # Show the plot
    plt.tight_layout()
    plt.show()

# Example usage:
csv_file = "Redacted Full Stories - MDS Capstone.csv"

# create_top_10_tags_bar_graph(csv_file)
create_top_10_count_bar_graph(csv_file, "Prison", 'Top 10 Counts of Stories per Prison (Descending Order)', 100)

create_top_10_count_bar_graph(csv_file, "Unique ID", 'Counts of Stories per Unique ID (Descending Order)')

create_top_10_count_bar_graph(csv_file, "Storyteller", 'Counts of Stories per Storyteller (Descending Order)')

create_top_10_count_bar_graph(csv_file, "Letter/Call", 'Counts of Stories Letters/Call (Descending Order)')
