import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns
from src.util import constants
import matplotlib.pyplot as plt


def cramers_stat(confusion_matrix):
    if confusion_matrix.size != 0:
        chi2 = ss.chi2_contingency(confusion_matrix)[0]
        n = confusion_matrix.sum().sum()
        return np.sqrt(chi2 / (n * (min(confusion_matrix.shape) - 1)))
    return 0


# todo optimize
def get_column_pairs_by_cramers_coef(dataframe, min_coef=0, max_coef=1, verbose=True):
    result = []
    for x_column in dataframe:
        for y_column in dataframe:
            if x_column != y_column:
                confusion_matrix = pd.crosstab(dataframe[x_column], dataframe[y_column])
                cramers_coef = cramers_stat(confusion_matrix)
                if not (np.math.isnan(cramers_coef)) and min_coef <= cramers_coef <= max_coef:
                    result.append([x_column, y_column])
                    if verbose:
                        print('{}) {}-{} : {}'.format(len(result), x_column, y_column, cramers_coef))
    return result


def get_column_pairs_by_cramers_coef_opt(dataframe, min_coef=0, max_coef=1, verbose=False):
    result = []

    df_matrix = dataframe.T.as_matrix()
    for x_idx, x_column in enumerate(df_matrix):
        print('------------------------' + str(x_idx) + '------------------------')
        for y_idx, y_column in enumerate(df_matrix):
            if x_idx != y_idx:
                confusion_matrix = pd.crosstab(x_column, y_column)
                cramers_coef = cramers_stat(confusion_matrix.as_matrix())
                if not (np.math.isnan(cramers_coef)) and min_coef <= cramers_coef <= max_coef:
                    x_column_name = dataframe[[x_idx]].dtypes.index[0]
                    y_column_name = dataframe[[y_idx]].dtypes.index[0]
                    if not [y_column_name, x_column_name] in result:
                        result.append([x_column_name, y_column_name])
                    if verbose:
                        print('{}) {}-{} : {}'.format(len(result), x_column_name, y_column_name, cramers_coef))
    return result


def get_column_pairs_by_cramers_coef_opt_table(dataframe):
    result = []
    df_matrix = dataframe.T.as_matrix()
    for x_idx, x_column in enumerate(df_matrix):
        print(x_idx)
        row = []
        for y_idx, y_column in enumerate(df_matrix):
            confusion_matrix = pd.crosstab(x_column, y_column)
            cramers_coef = cramers_stat(confusion_matrix.as_matrix())
            row.append(cramers_coef)
        result.append(row)
    fig, ax = plt.subplots()
    ax = sns.heatmap(result)
    fig.savefig(constants.DATA + 'heatmap_with_allsame')
    return result
