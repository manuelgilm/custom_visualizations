import seaborn as sns 
import matplotlib.pyplot as plt


def create_distribution_plot(data, title, x_label, y_label):
    """Creates a distribution plot"""
    data_med = data.median()
    data_mean = data.mean()
    sns.distplot(data)
    plt.title(title, fontsize=17)
    plt.axvline(data_med, color='red', alpha=0.6, label='Median')
    plt.axvline(data_mean, color='green', alpha=0.6, label='Mean')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()

def compare_density_plot(data1, data2, label1, label2, title, x_label, y_label):
    """compare densities plot"""
    sns.kdeplot(data1, color = 'blue', shade = True, label = label1)
    sns.kdeplot(data2, color = 'red', shade = True, label = label2)
    plt.title(title, fontsize=17)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()

def create_correlation_matrix(data, title, figsize=(18,10)):
    """creates a correlation matrix"""
    plt.figure(figsize=figsize)
    sns.heatmap(data.corr(), annot=True, cmap='Blues')
    plt.title(title, fontsize=16)