from src.util import data_util, calc_util, constants
import datetime


def is_date(string):
    try:
        datetime.datetime.strptime(string, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def get_dates_from_column(column):
    dates = []
    for value in column:
        if isinstance(value, str):
            if is_date(value):
                dates.append(value)
    return dates


def get_column_dates_stats(dataframe, min_percentage, max_percentage):
    print('{}% - {}%'.format(min_percentage, max_percentage))
    for column in dataframe:
        column_dates = get_dates_from_column(dataframe[column])
        dates_len = len(column_dates)
        col_len = len(dataframe[column])
        date_of_col_percentage = calc_util.percentage(dates_len, col_len)
        if dates_len != 0:
            text = '{}/{} ({}%) - {}'.format(dates_len, col_len, round(date_of_col_percentage, 2), column)
            if min_percentage <= date_of_col_percentage < max_percentage:
                print(text)


df = data_util.get_dataframe(constants.DATA + 'no_empty_h_150.csv')

get_column_dates_stats(df, 0, 5)
get_column_dates_stats(df, 5, 10)
get_column_dates_stats(df, 10, 30)
get_column_dates_stats(df, 30, 100)
