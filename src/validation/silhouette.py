from matplotlib import pyplot as plt
from sklearn.metrics import silhouette_samples

from src.k_modes import k_modes
from src.util import constants, data_util
from src.validation import simple_matching, silhouette
import numpy as np


def precomputed_silhouette(distance_matrix, labels):
    return silhouette_samples(distance_matrix, labels, metric='precomputed')


def visualize(x_values, y_values, title):
    plt.xlabel('cluster amount')
    plt.ylabel('silhouette coefficient')
    plt.plot(x_values, y_values, label=title)
    plt.legend()
    plt.savefig(constants.SILHOUETTE_OUT + title)


def k_modes_silhouette_visualize(rows, columns, min_cluster_amount, max_cluster_amount):
    cluster_amounts = []
    silhouette_coefficients = []
    dataframe = data_util.get_dataframe(constants.DATA + 'no_ctx_duplicates_52.csv', max_rows=rows, max_columns=columns)
    title = str(rows) + 'x' + str(columns)
    for num_of_clusters in range(min_cluster_amount, max_cluster_amount):
        silhouette_scores = k_modes_silhouette(dataframe, num_of_clusters)
        cluster_amounts.append(num_of_clusters)
        silhouette_coefficients.append(np.mean(silhouette_scores))
    silhouette.v(cluster_amounts, silhouette_coefficients, title)


def k_modes_silhouette(dataframe, num_of_clusters):
    clusters = k_modes(num_of_clusters, dataframe.iloc[:, 1:].as_matrix())
    distance_matrix = simple_matching.get_dissimilarity_matrix(dataframe)
    silhouette_samples = silhouette.precomputed_silhouette(distance_matrix, clusters.labels_)
    print('for {} clusters silhouette score is: {}'.format(num_of_clusters + 2, round(np.mean(silhouette_samples), 3)))
    return silhouette_samples
