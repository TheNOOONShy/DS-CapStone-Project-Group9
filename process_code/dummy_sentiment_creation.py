import pandas as pd
import random

# Read the original CSV file
input_file = "Redacted Full Stories - MDS Capstone.csv"
df = pd.read_csv(input_file)

# Create a new DataFrame with "Story ID (prison_yyyymmdd_topic)" and random "sentiment" values
sentiments = [random.uniform(-1, 1) for _ in range(len(df))]
new_df = pd.DataFrame({
    "Story ID (prison_yyyymmdd_topic)": df["Story ID (prison_yyyymmdd_topic)"],
    "sentiment": sentiments
})

# Save the new DataFrame to a new CSV file
output_file = "dummy sentiment.csv"
new_df.to_csv(output_file, index=False)

print(f"New CSV file '{output_file}' has been created.")
