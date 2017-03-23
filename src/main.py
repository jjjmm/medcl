from src import k_modes, fp_growth, cramers_v
from src.util import constants, data_util, decorators

columns = 102
rows = 152
df_with_ids = data_util.get_dataframe(constants.SORTED_MED_DATA_MIN_PATH, max_rows=rows, max_columns=columns,
                                      with_namespaces=True, drop_duplicates=True)
df_no_ids = df_with_ids.iloc[:, 2:]


def get_columns_to_remove(pairs):
    unique_columns = []
    for pair in pairs:
        if pair[0] not in unique_columns:
            unique_columns.append(pair[1])
    return unique_columns


@decorators.measure_time
def preprocess(dataframe):
    # remove V13, since every value in this column is unique and it generates cr. coef 1.0 with eac column
    df_no_ids_and_V13 = dataframe.drop('V13', 1)
    ctx_duplicate_columns = cramers_v.get_column_pairs_by_cramers_coef(dataframe=df_no_ids_and_V13, min_coef=0.9, max_coef=1)
    columns_to_remove = get_columns_to_remove(ctx_duplicate_columns)
    print(columns_to_remove)
    df_no_ctx_duplicates = df_no_ids_and_V13.drop(columns_to_remove, axis=1)
    df_no_ctx_duplicates.to_csv(constants.DATA + 'no_ctx_duplicates_' + str(columns) + '.csv')


def cluster_and_validate():
    k_modes_cluster_dict = k_modes.k_modes_dict(cluster_amount=3, dataframe=df_no_ids)
    k_modes.log_k_modes_stats(k_modes_cluster_dict)
    fp_growth_patterns = fp_growth.fp_growth_as_dict(k_modes_cluster_dict, min_support=20)
    fp_growth.log_fp_growth_dict(fp_growth_patterns)


preprocess(df_no_ids)
