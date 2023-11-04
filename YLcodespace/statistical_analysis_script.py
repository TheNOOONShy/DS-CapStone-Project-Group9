
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

# Function to read data from a CSV file
def read_data(file_path):
    return pd.read_csv(file_path)

# Function to create a QQ plot
def qq_plot(data, variable):
    plt.figure(figsize=(10, 6))
    stats.probplot(data[variable], dist="norm", plot=plt)
    plt.title(f'Q-Q Plot for {variable}')
    plt.xlabel('Theoretical Quantiles')
    plt.ylabel('Sample Quantiles')
    plt.show()

# Function to perform Box-Cox transformation and plot the QQ plot
def boxcox_transformation_and_qq_plot(data, variable):
    # Since the minimum value is very close to 0, we can apply Box-Cox transformation directly
    # Box-Cox requires all data to be positive, the smallest positive float can ensure no zero values
    data_positive = data[variable] + 1e-10

    # Perform Box-Cox transformation
    transformed_data, _ = stats.boxcox(data_positive)

    # Create a QQ plot for the transformed data
    plt.figure(figsize=(10, 6))
    stats.probplot(transformed_data, dist="norm", plot=plt)
    plt.title(f'Q-Q Plot for Box-Cox Transformed {variable}')
    plt.xlabel('Theoretical Quantiles')
    plt.ylabel('Sample Quantiles')
    plt.show()

# Function to plot histogram and display descriptive statistics
def plot_histogram_and_describe(data, variable):
    # Plotting the histogram for the original data
    plt.figure(figsize=(10, 6))
    plt.hist(data[variable], bins=30, edgecolor='black')
    plt.title(f'Histogram of {variable} Data')
    plt.xlabel(variable)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    # Descriptive statistics for the original data
    descriptive_stats = data[variable].describe()
    print(f'Descriptive statistics for {variable}:\n', descriptive_stats)

# Function to perform square root transformation and plot the QQ plot
def sqrt_transformation_and_qq_plot(data, variable):
    # Perform square root transformation
    data[variable + '_Sqrt'] = data[variable].apply(np.sqrt)

    # QQ plot for the square root transformed data
    qq_plot(data, variable + '_Sqrt')

