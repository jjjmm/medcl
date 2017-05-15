from src.util import data_util, constants

def little_MCAR(df):
    pass

df = data_util.get_dataframe(constants.DATA + 'df_80_plus_no_cont_no_ctx_comp_dup.csv', max_rows=1000, max_columns=1000)
little_MCAR(df)
