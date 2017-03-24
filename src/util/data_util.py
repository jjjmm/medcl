import numpy as np
import pandas as pd


def generate_dummy(element_amount=10, dimensions=2, seed=None):
    """ Generating random numpy array based on element_amount and dimensions.
    To make data reproducible, seed should be specified """
    np.random.seed(seed)
    return np.random.random((element_amount, dimensions))


def get_array_from_csv(path, keep_names=None, delimiter=','):
    return np.genfromtxt(path, delimiter=delimiter, dtype=None, names=keep_names)


def get_dataframe(data_path, max_rows, max_columns, with_namespaces=False, drop_duplicates=False):
    df = pd.read_csv(data_path)
    reduced_data = df.ix[0:max_rows - 1, 0:max_columns - 1]
    if drop_duplicates:
        reduced_data = reduced_data.T.drop_duplicates().T
    if with_namespaces:
        for column in reduced_data.ix[:, 1:]:
            reduced_data[column] = str(column) + ':' + reduced_data[column].astype(str)
    return reduced_data
