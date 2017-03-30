from src.validation import simple_matching
from src.util import constants, data_util

dataframe = data_util.get_dataframe(constants.DATA + 'no_ctx_duplicates_52.csv', max_rows=50, max_columns=50)
simple_matching.simple_matching_coefficient(dataframe.iloc[0], dataframe.iloc[1])
