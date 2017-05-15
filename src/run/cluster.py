import numpy as np
import pandas as pd

from src import k_modes, fp_growth, hdbscan_demo
from src.util import constants, data_util, decorators, logger


@decorators.measure_time
def cluster_k_modes(df, k=3):
    k_modes_cluster_dict = k_modes.k_modes_dict(cluster_amount=k, dataframe=df)
    logger.log_k_modes_stats(k_modes_cluster_dict, 'k-modes stats:')
    return k_modes_cluster_dict


@decorators.measure_time
def cluster_hdbscan(df, min_cl_size=5):
    return hdbscan_demo.hdbscan_dict(df)


def clsuter_and_calc_mean_equality(df, k):
    first_c_result = cluster_k_modes(df, k)
    second_c_result = cluster_k_modes(df, k)
    return calc_mean_equality(first_c_result, second_c_result)


# todo refactor
def calc_mean_equality(first_c_result, second_c_result):
    equality_between_most_equal_clusters = []
    for key, first_result_element in first_c_result.items():
        first_result_element_ids = list(map(lambda r: r[0], first_result_element))
        equality_percentage = []
        for key, second_c_result_element in second_c_result.items():
            second_c_result_element_ids = list(map(lambda r: r[0], second_c_result_element))
            max_len = max(len(first_result_element_ids), len(second_c_result_element_ids))
            equal_elements = (list(set(first_result_element_ids).intersection(second_c_result_element_ids)))
            equality_percentage.append(100 * len(equal_elements) / max_len)
        equality_between_most_equal_clusters.append(max(equality_percentage))
    mean = np.mean(equality_between_most_equal_clusters)
    return mean


def cluster_stat(runs, df, k):
    global_clustering_mean = []
    for n in range(1, runs + 1):
        clustering_mean_equality = clsuter_and_calc_mean_equality(df, k)
        global_clustering_mean.append(clustering_mean_equality)
        print('{}) equality between clusters: {}'.format(n, clustering_mean_equality))
    print('mean clustering equality in {} runs: {}'.format(runs, np.mean(global_clustering_mean)))


def cluster_and_export(df, k=3):
    result = cluster_k_modes(df, k=k)
    for index, (key, value) in enumerate(result.items()):
        df = pd.DataFrame(value)
        df.to_csv(constants.CLUSTER_OUT + 'cluster_' + str(index + 1) + '.csv', index=False)


def k_modes_by_random_cols(df, runs, cols_amount, cluster_amount):
    print(cols_amount)
    for run in range(0, 30):
        sample_df = data_util.get_sampled(df, cols_amount)
        cluster_k_modes(sample_df, cluster_amount)


# df = data_util.get_dataframe(constants.DATA + 'df_80_plus_no_cont_no_ctx_comp_dup.csv', max_rows=1000, max_columns=1000)
# df.fillna(value='missing', inplace=True)
# cluster(df.astype(str))
# df = data_util.get_dataframe(constants.DATA + 'df_80_plus_no_cont_no_dup.csv', max_rows=1000, max_columns=1000)
# df.fillna(value='missing', inplace=True)
# cluster(df.astype(str))
# df = data_util.get_dataframe(constants.DATA + 'df_80_plus_no_cont.csv', max_rows=1000, max_columns=1000)
# df.fillna(value='missing', inplace=True)
# cluster(df.astype(str))
df = data_util.get_dataframe(constants.DATASETS + '1_679.csv', max_rows=1000, max_columns=1000)
df.fillna(value='missing', inplace=True)

cluster_k_modes(df.astype(str), 3)
cluster_k_modes(df.astype(str), 4)
# k_modes_by_random_cols(df.astype(str), 1, 189, 3)
# k_modes_by_random_cols(df.astype(str), 1, 20, 3)
# k_modes_by_random_cols(df.astype(str), 1, 40, 3)
# k_modes_by_random_cols(df.astype(str), 1, 80, 3)
# k_modes_by_random_cols(df.astype(str), 1, 123, 3)
#
# k_modes_by_random_cols(df.astype(str), 1, 220, 3)
# k_modes_by_random_cols(df.astype(str), 1, 210, 3)
# k_modes_by_random_cols(df.astype(str), 1, 240, 3)
# k_modes_by_random_cols(df.astype(str), 1, 280, 3)
# k_modes_by_random_cols(df.astype(str), 1, 300, 3)
# k_modes_by_random_cols(df.astype(str), 1, 320, 3)
# k_modes_by_random_cols(df.astype(str), 1, 340, 3)
# k_modes_by_random_cols(df.astype(str), 1, 380, 3)
# k_modes_by_random_cols(df.astype(str), 1, 400, 3)
# k_modes_by_random_cols(df.astype(str), 1, 130, 3)
# k_modes_by_random_cols(df.astype(str), 1, 140, 3)
# k_modes_by_random_cols(df.astype(str), 1, 150, 3)
# k_modes_by_random_cols(df.astype(str), 1, 160, 3)
# k_modes_by_random_cols(df.astype(str), 1, 170, 3)
# k_modes_by_random_cols(df.astype(str), 1, 180, 3)
# k_modes_by_random_cols(df.astype(str), 1, 190, 3)
# k_modes_by_random_cols(df.astype(str), 1, 200, 3)
# k_modes_by_random_cols(df.astype(str), 1, 300, 3)
# k_modes_by_random_cols(df.astype(str), 1, 400, 3)
# k_modes_by_random_cols(df.astype(str), 1, 500, 3)
# k_modes_by_random_cols(df.astype(str), 1, 600, 3)
# k_modes_by_random_cols(df.astype(str), 1, 700, 3)
# k_modes_by_random_cols(df.astype(str), 1, 800, 3)
# cluster(df.astype(str))
