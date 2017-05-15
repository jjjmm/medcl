import numpy as np
import pandas as pd
from src import cramers_v
from src.util import data_util, constants, date_util


def get_cramers_by_partition(dataframe):
    dataframe.fillna(value='missing', inplace=True)
    column_start = 1
    column_end = 27
    for i in range(1, 8):
        ctx_duplicate_pairs = cramers_v.get_column_pairs_by_cramers_coef_opt(dataframe.iloc[:, column_start:column_end], 0.90, 1)
        np.savetxt(constants.DATA + 'cramers_out/20_04/cramers_v_{}_{}.txt'.format(column_start, column_end), delimiter=',', fmt="%s",
                   X=ctx_duplicate_pairs)
        column_start += 27
        column_end += 27


def count_ctx_duplicates_appearance(dataframe):
    checked = []
    result = []
    for column in dataframe:
        for value in dataframe[[column]].values:
            if value not in checked:
                times = (dataframe == value).sum().sum()
                result.append([value[0], times])
                checked.append(value)
    return result


def get_cramers_by_partition_no_duplicates(dataframe):
    dataframe = dataframe.T.drop_duplicates().T
    dataframe = drop_all_same(dataframe)
    dataframe = drop_dates(dataframe)
    get_cramers_by_partition(dataframe)


def drop_all_same(df):
    nunique = df.apply(pd.Series.nunique)
    cols_to_drop = nunique[nunique == 1].index
    df = df.drop(cols_to_drop, axis=1)
    return df


def drop_dates(df_no_complete_duplicates):
    dates_to_drop = []
    for column in df_no_complete_duplicates:
        column_dates = date_util.get_dates_from_column(df_no_complete_duplicates[column])
        dates_len = len(column_dates)
        if dates_len != 0 and dates_len == df_no_complete_duplicates[column].count():
            print(column)
            dates_to_drop.append(column)
    return df_no_complete_duplicates.drop(dates_to_drop, axis=1)


def count_duplicate_columns(duplicate_pairs):
    counted_ctx_dupicates = count_ctx_duplicates_appearance(duplicate_pairs)
    sorted_counted_ctx_dupicates = sorted(counted_ctx_dupicates, key=lambda row: row[1])
    idx = 1
    for value in sorted_counted_ctx_dupicates:
        print('{}) {} - {}'.format(idx, value[0], value[1]))
        idx += 1


def get_columns_to_remove(pairs):
    unique_columns = []
    for pair in pairs:
        if pair[0] not in unique_columns:
            unique_columns.append(pair[1])
    return unique_columns


# get_cramers_by_partition_no_duplicates(data_util.get_dataframe(constants.DATA + 'dates_0_10_as_bool_150.csv'))
# count_duplicate_columns(data_util.get_dataframe(constants.DATA + 'cramers_out/no_complete_duplicates_2/cramers_v_all.txt', header=None))

# df = drop_all_same(df)
# get_cramers_by_partition(df)
# res = cramers_v.get_column_pairs_by_cramers_coef_opt_table(df.iloc[:, 1:])
# print('----------------------------------------------------------')
# print(len(res))
# np.savetxt(constants.DATA + 'heatmap', delimiter=',', X=res)

# df = data_util.get_dataframe(constants.DATA + 'df_80_plus_no_cont_no_dup.csv', drop_duplicates=True)
# pairs = data_util.get_dataframe(constants.DATA + 'cramers_out/20_04/all.txt', header=None)

# df.to_csv(constants.CLUSTER_OUT + 'df_80_plus_no_cont_no_ctx_comp_dup.csv', index=False)
