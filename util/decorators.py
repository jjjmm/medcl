import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('function "{f}" took: {t} seconds'.format(f=func.__name__, t=(end-start)))
    return wrapper
