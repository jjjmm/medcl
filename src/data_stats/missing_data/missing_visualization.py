import missingno as msno
from src.util import data_util, constants

df = data_util.get_dataframe(constants.DATA + 'original/original_150_allstring.csv').iloc[:, :]
dfc = df.copy()
df_no_ctx = data_util.get_dataframe(constants.DATASETS + '2_344.csv').iloc[:, :]
msno.matrix(df)