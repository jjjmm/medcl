import numpy as np
import pandas as pd
import scipy.stats as ss


# todo add min 5 rule
def cramers_stat(confusion_matrix):
    chi2 = ss.chi2_contingency(confusion_matrix, correction=False)[0]
    n = confusion_matrix.as_matrix().sum()
    return np.sqrt(chi2 / (n * (min(confusion_matrix.shape) - 1)))


# todo optimize
def get_column_pairs_by_cramers_coef(dataframe, min_coef=0, max_coef=1, verbose=True):
    result = []
    for x_column in dataframe:
        for y_column in dataframe:
            if x_column != y_column:
                confusion_matrix = pd.crosstab(dataframe[str(x_column)], dataframe[str(y_column)])
                cramers_coef = cramers_stat(confusion_matrix)
                if not (np.math.isnan(cramers_coef)) and min_coef <= cramers_coef <= max_coef:
                    result.append([x_column, y_column])
                    if verbose:
                        print('{}) {}-{} : {}'.format(len(result), x_column, y_column, cramers_coef))
    return result
