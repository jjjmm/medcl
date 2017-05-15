from matplotlib import pyplot as plt
from sklearn.metrics import silhouette_samples

import hdbscan
from src import k_modes, hac, hdbscan_demo
from src.util import constants, data_util, decorators
from src.validation import simple_matching
import numpy as np

from sklearn.metrics import silhouette_score


def precomputed_silhouette(distance_matrix, labels):
    return silhouette_samples(distance_matrix, labels, metric='precomputed')


def visualize(x_values, y_values, title, x_label='min cluster size', y_label='silhouette coefficient'):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x_values, y_values, label=title)
    plt.legend(loc='upper right')
    plt.savefig(constants.SILHOUETTE_OUT + '11_5/hdbscan/' + title)


def k_modes_silhouette_visualize(df, min_cluster_amount, max_cluster_amount, title):
    cluster_amounts = []
    silhouette_coefficients = []
    for num_of_clusters in range(min_cluster_amount, max_cluster_amount):
        print(num_of_clusters)
        silhouette_scores = k_modes_silhouette(df, num_of_clusters)
        cluster_amounts.append(num_of_clusters)
        silhouette_coefficients.append(np.mean(silhouette_scores))
    print(max(silhouette_coefficients))
    visualize(cluster_amounts, silhouette_coefficients, title)


def hdbscan_silhouette_visualize(df, min_cl_size_list, title):
    cluster_amounts = []
    silhouette_coefficients = []
    for min_cl_size in min_cl_size_list:
        silhouette_scores = hdbscan_silhouette(df, min_cl_size)
        cluster_amounts.append(min_cl_size)
        silhouette_coefficients.append(np.mean(silhouette_scores))
    print(max(silhouette_coefficients))
    visualize(cluster_amounts, silhouette_coefficients, title)


def k_modes_silhouette(dataframe, num_of_clusters):
    df_no_ids = dataframe.iloc[:, 1:]
    clusters = k_modes.k_modes(num_of_clusters, df_no_ids.as_matrix())
    distance_matrix = simple_matching.get_dissimilarity_matrix(df_no_ids)
    return silhouette_score_calc(clusters, distance_matrix)


@decorators.measure_time
def silhouette_score_calc(clusters, distance_matrix):
    return silhouette_score(distance_matrix, clusters.labels_, 'precomputed')


def hdbscan_silhouette(dataframe, min_cluster_size):
    df_no_ids = dataframe.iloc[:, 1:]
    distance_matrix = simple_matching.get_dissimilarity_matrix(df_no_ids)
    clusters = hdbscan.HDBSCAN(metric='precomputed', min_cluster_size=min_cluster_size).fit(distance_matrix)
    return silhouette_score(distance_matrix, clusters.labels_, 'precomputed')


def extract_df_with_high_silhouette_columns(initial_df, cols_amount, cluster_amount, min_silhouette_treshold, runs):
    columns = []
    for run in range(0, runs):
        sample_df = data_util.get_sampled(initial_df, cols_amount).iloc[:, 1:]
        ss = k_modes_silhouette(sample_df, cluster_amount)
        print(ss)
        if ss <= min_silhouette_treshold:
            print(sample_df.columns)
            for column in sample_df.columns:
                if column not in columns:
                    columns.append(column)
    idf = initial_df.drop(columns, axis=1)
    return idf


#
df = data_util.get_dataframe(constants.DATASETS + '4_10.csv', max_rows=1000, max_columns=1000, with_namespaces=True)
df.fillna(value='missing', inplace=True)
df = df.astype(str)
df.to_csv(constants.DATA + '4_10_arm.csv', index=False, header=False)

# extracted_df = extract_df_with_high_silhouette_columns(df, 10, 5, 0.25, 100)
# k_modes_silhouette(extracted_df, 3)
# pass

# df = data_util.get_dataframe(constants.DATASETS + '6_10.csv', with_namespaces=True, max_rows=1000, max_columns=1000, header=None)
# df.fillna(value='missing', inplace=True)
# df.to_csv(constants.DATA + 'df_80_plus_no_cont_no_ctx_comp_dup_as_str_no_header.csv', index=False, header=False)
#
# amount_of_cols_list = [3, 5, 10, 20, 50, 90, 120]
# silhoutte_means = []
# for amount_of_cols in amount_of_cols_list:
#     silh_mean = mean_hdbscan_silhouette_by_random_cols(df, 40, amount_of_cols, 5)
#     silhoutte_means.append(silh_mean)
#     print('mean: {}'.format(silh_mean))
# visualize(amount_of_cols_list, silhoutte_means, 'dist_by_random_cols_k_10', 'amount of cols', 'silhouette mean')
# k_modes_silhouette_visualize(data_util.get_sampled(df, 80), 1000, 1000, 2, 3)
# # for i in range(0, 100):
# print('--------------------------{}------------------------'.format(3))
# silh_mean = mean_k_modes_silhouette_by_random_cols(df.astype(str), runs=20, cols_amount=3, cluster_amount=3)
# silhoutte_means.append(silh_mean)
# print('mean: {}'.format(round(silh_mean, 3)))


# df = data_util.get_dataframe(constants.DATASETS + '1_679.csv', with_namespaces=True, max_rows=1000, max_columns=1000)
# df.fillna(value='missing', inplace=True)
# k_modes_silhouette_visualize(df.astype(str), 3, 11, 'dataset 1')
# # df = data_util.get_dataframe(constants.DATASETS + '2_344.csv', with_namespaces=True, max_rows=1000, max_columns=1000)
# # df.fillna(value='missing', inplace=True)
# # k_modes_silhouette_visualize(df.astype(str), 3, 11, 'dataset 2')
#
# # df = data_util.get_dataframe(constants.DATASETS + '3_278.csv', with_namespaces=True, max_rows=1000, max_columns=1000)
# # df.fillna(value='missing', inplace=True)
# # k_modes_silhouette_visualize(df.astype(str), 3, 11, 'dataset 3')
#
# df = data_util.get_dataframe(constants.DATASETS + '4_123.csv', with_namespaces=True, max_rows=1000, max_columns=1000)
# df.fillna(value='missing', inplace=True)
# k_modes_silhouette_visualize(df.astype(str), 3, 11, 'dataset 2')
#
# df = data_util.get_dataframe(constants.DATASETS + '5_21.csv', with_namespaces=True, max_rows=1000, max_columns=1000)
# df.fillna(value='missing', inplace=True)
# k_modes_silhouette_visualize(df.astype(str), 3, 11, 'dataset 3')
# df = data_util.get_dataframe(constants.DATASETS + '6_10.csv', with_namespaces=True, max_rows=1000, max_columns=1000)
# df.fillna(value='missing', inplace=True)
# k_modes_silhouette_visualize(df.astype(str), 3, 11, 'dataset 4')
# # #
# hdbc_min_cl_size = [3, 5, 7, 9, 11, 13, 15, 17]
# #
# df = data_util.get_dataframe(constants.DATASETS + '1_679.csv', max_rows=1000, max_columns=1000)
# df.fillna(value='missing', inplace=True)
# hdbscan_silhouette_visualize(df.astype(str), hdbc_min_cl_size, 'dataset 1')
# # df = data_util.get_dataframe(constants.DATASETS + '2_344.csv', max_rows=1000, max_columns=1000)
# # df.fillna(value='missing', inplace=True)
# # hdbscan_silhouette_visualize(df.astype(str), hdbc_min_cl_size, 'dataset 2')
#
# # df = data_util.get_dataframe(constants.DATASETS + '3_278.csv', max_rows=1000, max_columns=1000)
# # df.fillna(value='missing', inplace=True)
# # hdbscan_silhouette_visualize(df.astype(str), hdbc_min_cl_size, 'dataset 2')
#
# df = data_util.get_dataframe(constants.DATASETS + '2_123.csv', max_rows=1000, max_columns=1000)
# df.fillna(value='missing', inplace=True)
# hdbscan_silhouette_visualize(df.astype(str), hdbc_min_cl_size, 'dataset 2')
#
# df = data_util.get_dataframe(constants.DATASETS + '3_21.csv', max_rows=1000, max_columns=1000)
# df.fillna(value='missing', inplace=True)
# hdbscan_silhouette_visualize(df.astype(str), hdbc_min_cl_size, 'dataset 3')
#
# df = data_util.get_dataframe(constants.DATASETS + '4_10.csv', max_rows=1000, max_columns=1000)
# df.fillna(value='missing', inplace=True)
# hdbscan_silhouette_visualize(df.astype(str), hdbc_min_cl_size, 'dataset 4')
