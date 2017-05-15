from src.util import data_util
from src.validation.silhouette import  hdbscan_silhouette
from src.validation.silhouette import  k_modes_silhouette

def columns_with_highest_hdbscan_silhouette(df, runs, cols_amount, min_cl_size):
    print('cols_amount: {}'.format(cols_amount))
    silhouette_coefficients = []
    mean_min = [1, '']
    mean_max = [0, '']
    for run in range(0, runs):
        sample_df = data_util.get_sampled(df, cols_amount)
        silhouette_scores = hdbscan_silhouette(sample_df, min_cl_size)
        mean = np.mean(silhouette_scores)
        silhouette_coefficients.append(mean)
        if mean < mean_min[0]:
            mean_min = [mean, sample_df.iloc[:, 1:].columns.values]
        if mean > mean_max[0]:
            mean_max = [mean, sample_df.iloc[:, 1:].columns.values]
    print('min: {} - {}'.format(round(mean_min[0], 3), ', '.join(mean_min[1])))
    print('max: {} - {}'.format(round(mean_max[0], 3), ', '.join(mean_max[1])))
    return mean_max[1]


def columns_with_highest_kmodes_silhouette(df, runs, cols_amount, cluster_amount):
    # print('cols_amount: {}'.format(cols_amount))
    silhouette_coefficients = []
    mean_min = [1, '']
    mean_max = [0, '']
    for run in range(0, runs):
        sample_df = data_util.get_sampled(df, cols_amount)
        silhouette_scores = k_modes_silhouette(sample_df, cluster_amount)
        mean = np.mean(silhouette_scores)
        silhouette_coefficients.append(mean)
        if mean < mean_min[0]:
            mean_min = [mean, sample_df.iloc[:, 1:].columns.values]
        if mean > mean_max[0]:
            mean_max = [mean, sample_df.iloc[:, 1:].columns.values]
    print('min: {} - {}'.format(round(mean_min[0], 3), ', '.join(mean_min[1])))
    print('max: {} - {}'.format(round(mean_max[0], 3), ', '.join(mean_max[1])))
    return np.mean(silhouette_coefficients)