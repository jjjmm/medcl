import numpy as np
import pandas as pd


def generate_dummy(element_amount=10, dimensions=2, seed=None):
    """ Generating random numpy array based on element_amount and dimensions.
    To make data reproducible, seed should be specified """
    np.random.seed(seed)
    return np.random.random((element_amount, dimensions))


def get_array_from_csv(path, keep_names=None, delimiter=','):
    return np.genfromtxt(path, delimiter=delimiter, dtype=None, names=keep_names)


def get_dataframe(data_path, max_rows, max_columns, with_namespaces=True):
    df = pd.read_csv(data_path)
    data_with_ids = df.ix[0:max_rows - 1, 0:max_columns - 1]
    if with_namespaces:
        for column in data_with_ids:
            data_with_ids[column] = str(column) + ':' + data_with_ids[column].astype(str)
    return data_with_ids
