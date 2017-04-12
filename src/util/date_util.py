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
