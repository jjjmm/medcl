from src.util import data_util, calc_util, constants, date_util


def get_column_dates_stats(dataframe, min_percentage, max_percentage, verbose=True):
    columns = []
    if verbose:
        print('{}% - {}%'.format(min_percentage, max_percentage))
    for column in dataframe:
        column_dates = date_util.get_dates_from_column(dataframe[column])
        dates_len = len(column_dates)
        col_len = len(dataframe[column])
        date_of_col_percentage = calc_util.percentage(dates_len, col_len)
        if dates_len != 0:
            if min_percentage <= date_of_col_percentage < max_percentage:
                if verbose:
                    text = '{}/{} ({}%) - {}'.format(dates_len, col_len, round(date_of_col_percentage, 2), column)
                    print(text)
                columns.append(column)
    return columns


def dates_to_bool(dataframe, columns):
    for column in columns:
        print(column)
        dataframe[column] = dataframe[column].map(lambda v: is_string_and_date(v))
    return dataframe


def is_string_and_date(v):
    if isinstance(v, str) and date_util.is_date(v):
        return 't'
    return 'f'


df = data_util.get_dataframe(constants.DATA + 'no_empty_h_150.csv')
date_columns = get_column_dates_stats(df, 0, 100, False)
dates_0_10_as_bool_150 = dates_to_bool(df, date_columns)
dates_0_10_as_bool_150.to_csv(constants.DATA + 'dates_0_100_as_bool_150.csv', index=False, encoding='UTF-8')
