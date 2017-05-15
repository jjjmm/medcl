from src.util import calc_util, data_util, constants


def percentage_nan(dataframe, whole=150, min_percentage=0, max_percentage=100):
    return ((min_percentage < calc_util.percentage(dataframe, whole)) &
            (max_percentage >= calc_util.percentage(dataframe, whole))).sum()


def percentage_nan_row(dataframe, whole=150, min_percentage=0, max_percentage=100):
    count = 0
    for row in dataframe:
        if (min_percentage < calc_util.percentage(row, whole)) and (max_percentage >= calc_util.percentage(row, whole)):
            count += 1
    return count


def percentage_nan_equals(dataframe, max_rows=150, equal_percentage=100):
    return (equal_percentage == calc_util.percentage(dataframe, max_rows)).sum()


df = data_util.get_dataframe(constants.DATA + '/df_80_plus_filled.csv')
max_columns = df.shape[1]
max_rows = df.shape[0]
overall = max_columns * max_rows
nan_by_column = df.isnull().sum()

nan_overall = nan_by_column.values.sum()
print('overall nan amount: {}/{}'.format(nan_overall, overall))
print('min nan amount: {}'.format(nan_by_column.min()))
print('max nan amount: {}'.format(nan_by_column.max()))

with_zero_missing = percentage_nan_equals(nan_by_column, equal_percentage=0)
print('0%: {}/{}'.format(with_zero_missing, max_rows))
print('100%: {}/{}'.format(percentage_nan_equals(nan_by_column, equal_percentage=100), max_rows))

# df_no_empty = df.loc[:, df.isnull().sum() != 150]
df_no_empty_nan_by_column = df.isnull().sum()
df_no_empty_nan_by_rows = df.isnull().sum(axis = 1)
max_columns = df.shape[1]
max_rows = df.shape[0]

print('nan by columns:')
print('-------------------------------------------')
print('0-5%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=0, max_percentage=5) + with_zero_missing, max_columns))
print('5-10%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=5, max_percentage=10), max_columns))
print('10-20%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=10, max_percentage=20), max_columns))
print('20-30%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=20, max_percentage=30), max_columns))
print('30-40%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=30, max_percentage=40), max_columns))
print('40-50%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=40, max_percentage=50), max_columns))
print('50-60%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=50, max_percentage=60), max_columns))
print('60-70%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=60, max_percentage=70), max_columns))
print('70-80%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=70, max_percentage=80), max_columns))
print('80-90%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=80, max_percentage=90), max_columns))
print('90-100%: {}/{}'.format(percentage_nan(df_no_empty_nan_by_column, min_percentage=90, max_percentage=100), max_columns))

print('nan by rows:')
print('-------------------------------------------')
with_zero_missing = percentage_nan_equals(df_no_empty_nan_by_rows, equal_percentage=0)
print('0%: {}/{}'.format(with_zero_missing, max_rows))
print('0-5%: {}/{}'.format(percentage_nan_row(df_no_empty_nan_by_rows, min_percentage=0, max_percentage=5, whole=max_columns), max_rows))
print('5-10%: {}/{}'.format(percentage_nan_row(df_no_empty_nan_by_rows, min_percentage=5, max_percentage=10, whole=max_columns), max_rows))
print('10-20%: {}/{}'.format(percentage_nan_row(df_no_empty_nan_by_rows, min_percentage=10, max_percentage=20, whole=max_columns), max_rows))
print('20-30%: {}/{}'.format(percentage_nan_row(df_no_empty_nan_by_rows, min_percentage=20, max_percentage=30, whole=max_columns), max_rows))
print('30-40%: {}/{}'.format(percentage_nan_row(df_no_empty_nan_by_rows, min_percentage=30, max_percentage=40, whole=max_columns), max_rows))
print('40-50%: {}/{}'.format(percentage_nan_row(df_no_empty_nan_by_rows, min_percentage=40, max_percentage=50, whole=max_columns), max_rows))
print('50-60%: {}/{}'.format(percentage_nan_row(df_no_empty_nan_by_rows, min_percentage=50, max_percentage=60, whole=max_columns), max_rows))
print('60-70%: {}/{}'.format(percentage_nan_row(df_no_empty_nan_by_rows, min_percentage=60, max_percentage=70, whole=max_columns), max_rows))
print('70-80%: {}/{}'.format(percentage_nan_row(df_no_empty_nan_by_rows, min_percentage=70, max_percentage=80, whole=max_columns), max_rows))
print('80-90%: {}/{}'.format(percentage_nan_row(df_no_empty_nan_by_rows, min_percentage=80, max_percentage=90, whole=max_columns), max_rows))
print('90-100%: {}/{}'.format(percentage_nan_row(df_no_empty_nan_by_rows, min_percentage=90, max_percentage=100, whole=max_columns), max_rows))

df = data_util.get_dataframe(constants.DATA + 'dates_0_100_as_bool_150.csv')
df_no_99 = df.isnull().sum() >= 30
to_drop =[]
for v, k in df_no_99.items():
    if k:
        to_drop.append(v)
df = df.drop(to_drop, 1)

df.to_csv(constants.DATA + 'df_80_plus_filled.csv', index=False, encoding='UTF-8')
