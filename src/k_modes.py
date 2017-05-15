from kmodes import kmodes


def k_modes(cluster_amount, data):
    km = kmodes.KModes(n_clusters=cluster_amount, init='Huang', n_init=10, verbose=0)
    return km.fit(data)


def as_dict(data, clusters, cluster_indices):
    data_dict = {}
    for cluster_index in range(0, cluster_indices):
        data_array = []
        for d, c in zip(data, clusters):
            if c == cluster_index:
                data_array.append(d)
        data_dict[cluster_index] = data_array
    return data_dict


def k_modes_dict(cluster_amount, dataframe):
    df_no_ids = dataframe.iloc[:, 1:]
    data_matrix = df_no_ids.as_matrix()
    clusters = k_modes(cluster_amount, data_matrix)
    return as_dict(dataframe.as_matrix(), clusters.labels_, cluster_amount)



