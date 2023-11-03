
import pandas as pd
import matplotlib.pyplot as plt

# Load your data
data = pd.read_csv('/Users/youli/Desktop/UC_Irvine/FQ_2023/DS-CapStone-Project-Group9/Analysis_CSVs/sentiment_analysis_results.csv')

# Bar chart for average sentiment intensity
mean_sentiments = data[['Negative Sentiment', 'Neutral Sentiment', 'Positive Sentiment']].mean()
plt.figure(figsize=(10,6))
mean_sentiments.plot(kind='bar', color=['red', 'gray', 'green'])
plt.title('Average Sentiment Intensity Distribution')
plt.ylabel('Average Intensity')
plt.xlabel('Sentiment Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Histogram for Compound Sentiment distribution
plt.figure(figsize=(10,6))
plt.hist(data['Compound Sentiment'], bins=30, color='blue', alpha=0.7)
plt.title('Compound Sentiment Intensity Distribution')
plt.xlabel('Compound Sentiment Intensity')
plt.ylabel('Number of Files')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()





