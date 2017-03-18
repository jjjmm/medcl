"""Hierarchical Agglomerative Clustering"""

from util import visualization_util
from scipy.cluster.hierarchy import linkage


def cluster_with_dendrogram(data, distance_metric='ward', x_axis='x', y_axis='y'):
    linked_data = cluster(data, distance_metric)
    visualization_util.show_dendrogram(linked_data, 'hac', x_axis, y_axis)


def cluster(data, distance_metric='ward'):
    return linkage(data, distance_metric)
