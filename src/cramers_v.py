import numpy as np
import pandas as pd
import scipy.stats as ss


# todo add min 5 rule
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
                        print('{}) {}-{} : {}'.format(len(result), x_column+1, y_column+1, cramers_coef))
    return result


def get_column_pairs_by_cramers_coef_opt(dataframe, min_coef=0, max_coef=1, verbose=True):
    result = []
    df_matrix = dataframe.T.as_matrix()
    for x_idx, x_column in enumerate(df_matrix):
        for y_idx, y_column in enumerate(df_matrix):
            if x_idx != y_idx:
                confusion_matrix = pd.crosstab(df_matrix[7], dataframe[8])
                cramers_coef = cramers_stat(confusion_matrix.as_matrix())
                if not (np.math.isnan(cramers_coef)) and min_coef <= cramers_coef <= max_coef:
                    result.append([x_column, y_column])
                    if verbose:
                        print('{}) {}-{} : {}'.format(len(result), x_idx+1, y_idx+1, cramers_coef))
    return result
