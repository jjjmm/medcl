import numpy as np
from src.util import data_util, constants
from src import cramers_v


def get_cramers_by_partition(dataframe):
    dataframe.fillna(value='missing', inplace=True)
    column_start = 1
    column_end = 46
    for i in range(1, 11):
        print('{}-{}'.format(column_start,column_end))
        ctx_duplicate_pairs = cramers_v.get_column_pairs_by_cramers_coef_opt(dataframe.iloc[:, column_start:column_end], 1, 1, True)
        np.savetxt(constants.DATA + 'cramers_out/cramers_v_{}_{}.txt'.format(column_start, column_end), delimiter=',', fmt="%s",
                   X=ctx_duplicate_pairs)
        column_start += 46
        column_end += 46


# df = data_util.get_dataframe(constants.DATA + 'dates_0_10_as_bool_150.csv')
# complete_duplicates = df.T.duplicated(keep='first')
# df_no_complete_duplicates = df.T.drop_duplicates()
# get_cramers_by_partition(df_no_complete_duplicates.T)
# df_no_complete_duplicates.T.to_csv(constants.CLUSTER_OUT + 'no_complete_duplicates.csv', index=False, header=False, encoding='UTF-8')
# print('complete duplicates: {}/{}'.format(complete_duplicates.sum(), df.shape[1]))
no_ctx_duplicates = data_util.get_dataframe(constants.DATA + 'cramers_out/no_complete_duplicates/cramers_v_all.txt', header=None)
print(no_ctx_duplicates)