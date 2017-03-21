from kmodes import kmodes
from termcolor import colored


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


def k_modes_dict(cluster_amount, dataframe):
    """returns a dict with cluster id as key and data as value"""
    data_matrix = dataframe.as_matrix()
    clusters = k_modes(cluster_amount, data_matrix)
    return as_dict(data_matrix, clusters.labels_, cluster_amount - 1)


def log_k_modes_dict(k_modes_cluster_dict):
    print(colored('k-modes stats:', 'green'))
    for key, value in k_modes_cluster_dict.items():
        print('cluster {} contains {} data points'.format(str(key), len(value)))
