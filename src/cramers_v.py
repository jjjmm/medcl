import numpy as np
import pandas as pd
import scipy.stats as ss


def cramers_stat(confusion_matrix):
    chi2 = ss.chi2_contingency(confusion_matrix, correction=False)[0]
    n = confusion_matrix.as_matrix().sum()
    return np.sqrt(chi2 / (n * (min(confusion_matrix.shape) - 1)))


def print_by_cramers_index(dataframe, min_index=0, max_index=1):
    for x_column in dataframe:
        for y_column in dataframe:
            if x_column != y_column:
                confusion_matrix = pd.crosstab(dataframe[str(x_column)], dataframe[str(y_column)])
                result = cramers_stat(confusion_matrix)
                if not (np.math.isnan(result)) and min_index < result < max_index:
                    print(str(x_column) + '-' + str(y_column) + ':' + str(result))
