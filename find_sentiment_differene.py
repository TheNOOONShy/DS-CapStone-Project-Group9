import pandas as pd

# Read in the two CSV files
vader_file = "sentiment_analysis_results.csv"
flair_file = "sentiment_analysis_results_flair.csv"

vader_df = pd.read_csv(vader_file)
flair_df = pd.read_csv(flair_file)

# Merge the data from the two DataFrames using the "Filename" column
merged_df = vader_df.merge(flair_df, on="Filename", how="inner")

# Create the new DataFrame with the specified conditions
merged_df["NegVaderPosFlair"] = (merged_df["Compound Sentiment"] < 0) & (merged_df["Sentiment"] == "POSITIVE")
merged_df["PosVaderNegFlair"] = (merged_df["Compound Sentiment"] > 0) & (merged_df["Sentiment"] == "NEGATIVE")
merged_df["MatchingVaderFlair"] = ((merged_df["Compound Sentiment"] > 0) & (merged_df["Sentiment"] == "POSITIVE")) | ((merged_df["Compound Sentiment"] < 0) & (merged_df["Sentiment"] == "NEGATIVE"))

# # Convert the Boolean columns to "True" or "False" strings
# merged_df["NegVaderPosFlair"] = merged_df["NegVaderPosFlair"].map({True: "True", False: "False"})
# merged_df["PosVaderNegFlair"] = merged_df["PosVaderNegFlair"].map({True: "True", False: "False"})
# merged_df["MatchingVaderFlair"] = merged_df["MatchingVaderFlair"].map({True: "True", False: "False"})

# Select and reorder columns
result_df = merged_df[["Filename", "NegVaderPosFlair", "PosVaderNegFlair", "MatchingVaderFlair"]]

# Save the results to a new CSV file
output_file = "sentiment_analysis_results_combined.csv"
result_df.to_csv(output_file, index=False)

print("Results saved to", output_file)
