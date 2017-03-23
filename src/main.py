from src import k_modes, fp_growth, cramers_v
from src.util import constants, data_util, decorators

df_with_ids = data_util.get_dataframe(constants.SORTED_MED_DATA_MIN_PATH, 150, 402, with_namespaces=True)
df_no_ids = df_with_ids.iloc[:, 2:]


def get_duplicate_columns(pairs):
    unique_columns = []
    for pair in pairs:
        if pair[0] not in unique_columns:
            unique_columns.append(pair[1])
    return unique_columns


@decorators.measure_time
def preprocess():
    # remove V13, since every value in this column is unique and it generates cr. coef 1.0 with eac column
    df_no_ids_and_V13 = df_no_ids.drop('V13', 1)
    """discovering complete duplicates with cramer's coefficient = 1.0
        327 pairs 1.0 (100 dimensions)
        555 pairs 1.0 (200 dimensions)"""
    duplicate_pairs = cramers_v.get_unique_pairs_by_cramers_coef(dataframe=df_no_ids_and_V13, min_coef=1, max_coef=1)
    print(get_duplicate_columns(duplicate_pairs))
    print(len(get_duplicate_columns(duplicate_pairs)))


def cluster_and_validate():
    k_modes_cluster_dict = k_modes.k_modes_dict(cluster_amount=3, dataframe=df_no_ids)
    k_modes.log_k_modes_stats(k_modes_cluster_dict)
    fp_growth_patterns = fp_growth.fp_growth_as_dict(k_modes_cluster_dict, min_support=20)
    fp_growth.log_fp_growth_dict(fp_growth_patterns)


preprocess()
