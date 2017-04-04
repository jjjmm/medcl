from src.util import data_util, constants
from src import cramers_v

df = data_util.get_dataframe(constants.DATA + 'no_empty_150.csv', header=None)
complete_duplicates = df.T.duplicated(keep='first')
print('complete duplicates: {}/{}'.format(complete_duplicates.sum(), df.shape[1]))
# df_no_complete_duplicates = df.T.drop_duplicates()
# df_no_complete_duplicates.T.to_csv(constants.CLUSTER_OUT + 'no_complete_duplicates.csv', index=False, header=False, encoding='UTF-8')
df_no_complete_duplicates = data_util.get_dataframe(constants.DATA + 'no_complete_duplicates_150.csv', header=None)
cramers_v.get_column_pairs_by_cramers_coef(df_no_complete_duplicates, 1, 1, True)