import pandas as pd


file_path = '~/Desktop/UC_Irvine/FQ_2023/DS-CapStone-Project-Group9/Analysis CSVs/sentiment_analysis_results_flair.csv'

# Load the CSV file
data = pd.read_csv(file_path)

# Apply the transformation to the Polarity column
data['Polarity'] = data.apply(
    lambda row: 1 - row['Polarity'] if row['Sentiment'] == 'NEGATIVE' else row['Polarity'],
    axis=1
)

# Save the transformed data to a new CSV file
transformed_file_path = 'transformed_flair.csv'
data.to_csv(transformed_file_path, index=False)

