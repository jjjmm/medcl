from src.util import data_util, constants


def percentage_nan(dataframe, max_rows=150, min_percentage=0, max_percentage=100):
    return ((min_percentage < percentage(dataframe, max_rows)) &
            (max_percentage >= percentage(dataframe, max_rows))).sum()


def percentage_nan_equals(dataframe, max_rows=150, equal_percentage=100):
    return (equal_percentage == percentage(dataframe, max_rows)).sum()


def percentage(part, whole):
    return part / whole * 100


df = data_util.get_dataframe(constants.DATA + 'original_150_allstring.csv', header=None)
max_rows = df.shape[1]
overall = df.shape[0] * max_rows
nan_by_column = df.isnull().sum()

nan_overall = nan_by_column.values.sum()
print('overall nan amount: {}/{}'.format(nan_overall, overall))
print('min nan amount: {}'.format(nan_by_column.min()))
print('max nan amount: {}'.format(nan_by_column.max()))

print('0%: {}/{}'.format(percentage_nan_equals(nan_by_column, equal_percentage=0), max_rows))
print('100%: {}/{}'.format(percentage_nan_equals(nan_by_column, equal_percentage=100), max_rows))

df_no_empty = df.loc[:, df.isnull().sum() != 150]
df_no_empty_nan_by_column = df_no_empty.isnull().sum()
print('-------------------------------------------')
print('0-5%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=0, max_percentage=5) + 101, max_rows))
print('5-10%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=5, max_percentage=10), max_rows))
print('10-20%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=10, max_percentage=20), max_rows))
print('20-30%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=20, max_percentage=30), max_rows))
print('30-40%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=30, max_percentage=40), max_rows))
print('40-50%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=40, max_percentage=50), max_rows))
print('50-60%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=50, max_percentage=60), max_rows))
print('60-70%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=60, max_percentage=70), max_rows))
print('70-80%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=70, max_percentage=80), max_rows))
print('80-90%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=80, max_percentage=90), max_rows))
print('90-100%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=90, max_percentage=100), max_rows))
