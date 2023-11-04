from csv_counter import count
from statistical_analysis_script import (read_data, plot_histogram_and_describe, qq_plot, 
                           sqrt_transformation_and_qq_plot, boxcox_transformation_and_qq_plot)



if __name__ == "__main__":
    file_path = '/Users/youli/Desktop/UC_Irvine/FQ_2023/DS-CapStone-Project-Group9/Analysis CSVs/merged3files.csv'
    
    data = read_data(file_path)
    plot_histogram_and_describe(data, 'Polarity')
    qq_plot(data, 'Polarity')
    sqrt_transformation_and_qq_plot(data, 'Polarity')
    boxcox_transformation_and_qq_plot(data, 'Polarity')
    

