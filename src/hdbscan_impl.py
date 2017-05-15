from src.validation import simple_matching
from src.util import data_util, logger, decorators
import hdbscan
import seaborn as sns
import matplotlib.pyplot as plt


def hdbscan_dict(df, visualize_tree=False, log=False):
    df_no_ids = df.iloc[:, 1:]
    distance_matrix = simple_matching.get_dissimilarity_matrix_opt(df_no_ids)
    clusters = hdbscan_clusters(distance_matrix)
    if visualize_tree:
        clusters.condensed_tree_.plot(select_clusters=True,
                                      selection_palette=sns.color_palette('deep', 8))
        plt.show()
    cluster_dict = data_util.as_dict(df.as_matrix(), clusters.labels_)
    if log:
        logger.log_k_modes_stats(cluster_dict, 'hdbscan clust:')
    return cluster_dict


@decorators.measure_time
def hdbscan_clusters(distance_matrix):
    return hdbscan.HDBSCAN(metric='precomputed', min_cluster_size=5).fit(distance_matrix)

# df = data_util.get_dataframe(constants.DATASETS + '6_10.csv', max_rows=1000, max_columns=1000)
# df.fillna(value='missing', inplace=True)
# cluster_dist = hdbscan_dict(df, False)
# pass
# clusterer.single_linkage_tree_.plot()
# plt.show()
# print('b')
# fig, ax = plt.subplots()
# ax = sns.distplot(clusterer.outlier_scores_[np.isfinite(clusterer.outlier_scores_)], rug=True)
# # fig.savefig(constants.DATA + 'hdbscan/outliers')
