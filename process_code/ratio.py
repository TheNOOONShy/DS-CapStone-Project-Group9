

import pandas as pd

def process_data(input_file_path, output_file_path):

    weekly_data = pd.read_csv(input_file_path)


    grouped_data = weekly_data.groupby(['Facility Name', 'Week Label'])


    positive_count = grouped_data['Flair_Sentiment_Indicator'].apply(lambda x: (x == 1).sum()).rename('Positive_Count')
    negative_count = grouped_data['Flair_Sentiment_Indicator'].apply(lambda x: (x == 0).sum()).rename('Negative_Count')


    overall_count = weekly_data.groupby('Week Label')['Flair_Sentiment_Indicator'].count().rename('Overall Count')
    prison_count = grouped_data['Flair_Sentiment_Indicator'].count().rename('Prison Count')


    merged_data = pd.concat([positive_count, negative_count, prison_count], axis=1).reset_index()
    merged_data = merged_data.merge(overall_count, on='Week Label')


    merged_data['Overall Positive Ratio'] = merged_data['Positive_Count'] / merged_data['Overall Count']
    merged_data['Overall Negative Ratio'] = merged_data['Negative_Count'] / merged_data['Overall Count']
    merged_data['Prison Positive Ratio'] = merged_data['Positive_Count'] / merged_data['Prison Count']
    merged_data['Prison Negative Ratio'] = merged_data['Negative_Count'] / merged_data['Prison Count']

    final_table = merged_data[['Facility Name', 'Week Label', 'Positive_Count', 'Negative_Count', 
                               'Overall Count', 'Prison Count', 'Overall Positive Ratio', 
                               'Overall Negative Ratio', 'Prison Positive Ratio', 'Prison Negative Ratio']]


    final_table.to_csv(output_file_path, index=False)

    print("Data processed and saved successfully.")


input_file_path = 'weeklydata.csv'  
output_file_path = 'ratio_by_Facility.csv'  


process_data(input_file_path, output_file_path)
