from src import k_modes, fp_growth, cramers_v
from src.util import constants, data_util, decorators
import numpy as np
import pandas as pd

columns = 52
rows = 152


def get_columns_to_remove(pairs):
    unique_columns = []
    for pair in pairs:
        if pair[0] not in unique_columns:
            unique_columns.append(pair[1])
    return unique_columns


@decorators.measure_time
def preprocess(dataframe):
    df_no_V13 = dataframe.drop('V13', 1)
    df_no_ids = df_no_V13.iloc[:, 1:]
    # remove V13, since every value in this column is unique and it generates cr. coef 1.0 with eac column
    ctx_duplicate_columns = cramers_v.get_column_pairs_by_cramers_coef(dataframe=df_no_ids, min_coef=0.9, max_coef=1)
    columns_to_remove = get_columns_to_remove(ctx_duplicate_columns)
    print(columns_to_remove)
    df_no_ctx_duplicates = df_no_V13.drop(columns_to_remove, axis=1)
    df_no_ctx_duplicates.to_csv(constants.DATA + 'no_ctx_duplicates_' + str(columns) + '.csv')


def cluster_and_validate(dataframe):
    k_modes_cluster_dict = cluster(dataframe)
    validate(k_modes_cluster_dict)


def validate(k_modes_cluster_dict):
    fp_growth_patterns = fp_growth.fp_growth_as_dict(k_modes_cluster_dict, min_support=20)
    fp_growth.log_fp_growth_dict(fp_growth_patterns)


def cluster(dataframe):
    k_modes_cluster_dict = k_modes.k_modes_dict(cluster_amount=3, dataframe=dataframe)
    k_modes.log_k_modes_stats(k_modes_cluster_dict)
    return k_modes_cluster_dict


# df_with_ids = data_util.get_dataframe(constants.SORTED_MED_DATA_MIN_PATH, max_rows=rows, max_columns=columns,
#                                       with_namespaces=True, drop_duplicates=True)
# preprocess(df_with_ids)
def clsuter_and_calc_mean_equality():
    first_c_result = cluster(data_util.get_dataframe(constants.DATA + 'no_ctx_duplicates_52.csv', max_rows=rows, max_columns=columns))
    second_c_result = cluster(data_util.get_dataframe(constants.DATA + 'no_ctx_duplicates_52.csv', max_rows=rows, max_columns=columns))
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


def cluster_stat(runs):
    global_clustering_mean = []
    for n in range(1, runs + 1):
        clustering_mean_equality = clsuter_and_calc_mean_equality()
        global_clustering_mean.append(clustering_mean_equality)
        print('{}) equality between clusters: {}'.format(n, clustering_mean_equality))
    print('mean clustering equality in {} runs: {}'.format(runs, np.mean(global_clustering_mean)))


def cluster_and_export():
    result = cluster(data_util.get_dataframe(constants.DATA + 'no_ctx_duplicates_52.csv', max_rows=rows, max_columns=columns))
    for index, (key, value) in enumerate(result.items()):
        df = pd.DataFrame(value)
        df.to_csv(constants.CLUSTER_OUT + 'cluster_' + str(index+1) + '.csv', index=False, header=False)


cluster_and_export()
# cluster_stat(10)
# cluster_stat(20)
# cluster_stat(30)
