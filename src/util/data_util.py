import numpy as np
import pandas as pd


def generate_dummy(element_amount=10, dimensions=2, seed=None):
    """ Generating random numpy array based on element_amount and dimensions.
    To make data reproducible, seed should be specified """
    np.random.seed(seed)
    return np.random.random((element_amount, dimensions))


def get_array_from_csv(path, keep_names=None, delimiter=','):
    return np.genfromtxt(path, delimiter=delimiter, dtype=None, names=keep_names)


def get_dataframe(data_path, max_rows=10000, max_columns=10000, with_namespaces=False, drop_duplicates=False, header=0):
    df = pd.read_csv(data_path, header=header, encoding='ISO-8859-1')
    reduced_data = df.ix[0:max_rows - 1, 0:max_columns - 1]
    if drop_duplicates:
        reduced_data = reduced_data.T.drop_duplicates().T
    if with_namespaces:
        for column in reduced_data.ix[:, 1:]:
            reduced_data[column] = str(column).replace(" ", "") + ':' + reduced_data[column].astype(str)
    return reduced_data


def get_sampled(dataframe, dim_amount):
    df_no_id = dataframe.iloc[:, 1:]
    columns = np.random.choice(df_no_id.columns, dim_amount)
    id_column_values = dataframe[[0]].values
    id_column_name = dataframe.columns[0]
    sampled_df = df_no_id[columns]
    sampled_df.insert(0, id_column_name, id_column_values)
    return sampled_df


def as_dict(data, labels):
    data_dict = {}
    for cluster_index in set(labels):
        data_array = []
        for d, c in zip(data, labels):
            if c == cluster_index:
                data_array.append(d)
        data_dict[cluster_index] = data_array
    return data_dict


def convert_categories_to_numbers(df):
    for column in df:
        cc = pd.Categorical(df[column])
        df[column] = cc.codes
    return df


def generate_random_dataset_with_respect_to_categories(df, rows):
    df_new = pd.copy(df)
    for column in df:
        min_cat = min(np.nanmin(df[column]))
        max_cat = max(np.nanmax(df[column]))
        print('yo')
        try:
            df_new[column] = np.random.choice(range(int(min_cat), int(max_cat) + 1), rows)
        except ValueError:
            print('hello')


