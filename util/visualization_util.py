from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram


def show_dendrogram(data, title, xlabel, ylabel):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    dendrogram(data)
    plt.show()
