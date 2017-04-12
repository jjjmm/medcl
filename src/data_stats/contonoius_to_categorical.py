from src.util import data_util, constants

df = data_util.get_dataframe(constants.DATA + 'df_no_99.csv')
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

newdf = df.select_dtypes(include=numerics)

likely_cat = {}
for var in newdf.columns:
    likely_cat[var] = 1. * df[var].nunique() / df[var].count()
for v, k in likely_cat.items():
    if k >= 0.6:
        print('{}'.format(v))
