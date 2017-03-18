from kmodes import kmodes
from util import print_util, data_util


def k_modes(cluster_amount, data):
    km = kmodes.KModes(n_clusters=cluster_amount, init='Huang', n_init=1, verbose=1)
    return km.fit(data)


# todo refactor
def as_dict(data, clusters, cluster_indices):
    data_dict = {}
    for cluster_index in range(0, cluster_indices + 1):
        data_array = []
        for d, c in zip(data, clusters):
            if c == cluster_index:
                data_array.append(list(map(str, d.tolist())))
        data_dict[cluster_index] = data_array
    return data_dict


# todo implement string correlation, corr coefficient
def filter_by_correlation_coefficient(data):
    pass


def k_modes_dict(cluster_amount, data_path, max_rows=10, max_columns=10, verbose=True):
    """returns a dict with cluster id as key and data as value"""
    data_with_ids = data_util.get_dataframe(data_path, max_rows, max_columns)
    data_without_ids = data_with_ids.ix[:, 2:].as_matrix()
    clusters = k_modes(cluster_amount, data_without_ids)
    if (verbose):
        print_k_modes_data(clusters, data_with_ids, data_without_ids)
    return as_dict(data_without_ids, clusters.labels_, cluster_amount - 1)


def print_k_modes_data(clusters, data_with_ids, data_without_ids):
    print_util.print_pair('data with ids', data_with_ids)
    print_util.print_pair('data without ids', data_without_ids)
    print_util.print_pair('clusters', clusters.labels_)
