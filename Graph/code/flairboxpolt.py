import pandas as pd
import matplotlib.pyplot as plt



# Load the Flair data from your local path
flair_data = pd.read_csv('/Users/youli/Desktop/UC_Irvine/FQ_2023/DS-CapStone-Project-Group9/Analysis_CSVs/sentiment_analysis_results_flair.csv') 

# Separate the data based on sentiment
negative_sentiments = flair_data[flair_data['Sentiment'] == 'NEGATIVE']['Polarity']
positive_sentiments = flair_data[flair_data['Sentiment'] == 'POSITIVE']['Polarity']

# Set up the figure
fig, ax = plt.subplots(figsize=(10, 6))

# Data to plot
data_to_plot_flair = [negative_sentiments, positive_sentiments]

# Create the boxplot
bp = ax.boxplot(data_to_plot_flair, patch_artist=True, notch=True, vert=True, showmeans=True)
colors = ['red', 'green']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Add annotations for median, max and min values
for i, line in enumerate(bp['medians']):
    x, y = line.get_xydata()[1]
    ax.annotate(f'Median: {y:.3f}', (x, y), textcoords="offset points", xytext=(10,-10), ha='center', fontsize=8)
for i, line in enumerate(bp['whiskers']):
    x, y = line.get_xydata()[1]
    label = 'Min: ' if i % 2 == 0 else 'Max: '
    ax.annotate(f'{label}{y:.3f}', (x, y), textcoords="offset points", xytext=(10,10 if label == "Min: " else -10), ha='center', fontsize=8)

# Set title and labels
ax.set_title('Boxplot of Sentiments (Flair)')
ax.set_xticklabels(['Negative Sentiment', 'Positive Sentiment'])
ax.set_ylabel('Polarity Score')

plt.tight_layout()
plt.show()




