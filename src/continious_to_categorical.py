from src.util import data_util, constants
import pandas as pd

df = data_util.get_dataframe(constants.DATA + 'df_no_99.csv')
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

newdf = df.select_dtypes(include=numerics)


def get_continious_column_names(df):
    likely_categories = {}
    categorical_columns = []
    for var in newdf.columns:
        likely_categories[var] = 1. * df[var].nunique() / df[var].count()
    for v, k in likely_categories.items():
        if k >= 0.6:
            categorical_columns.append(v)


def get_uniform_categorical_intervals(df, columns):
    for columns in columns:
        try:
            cat = pd.cut(df[columns], 5)
        except TypeError:
            print(columns)
        except KeyError:
            print(columns)
            continue
        print('changed like:{}'.format(columns))
        df[columns] = cat

get_continious_column_names()
df = data_util.get_dataframe(constants.DATA + 'df_90p_80p_filled.csv')


lines = [line.rstrip('\n') for line in open(constants.DATA + 'continious_to_categorical.txt')]


get_uniform_categorical_intervals()
