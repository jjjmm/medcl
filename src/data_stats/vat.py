import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from src.util import constants


def order(diss_matrix):
    """VAT: A Tool for Visual Assessment of (Cluster) Tendency. J.C. Bezdek, R.J. Hathaway
    dissimilarity matrix ordering algorithm implementation"""

    dm = np.matrix(diss_matrix)
    K = list(range(0, np.shape(dm)[0]))
    J = list(range(0, np.shape(dm)[0]))
    P = []
    I = []
    i_max = np.unravel_index(dm.argmax(), dm.shape)[0]
    J.remove(i_max)
    I.append(i_max)
    P.append(i_max)
    for r in range(1, len(K)):
        min = 1
        min_j = 0
        for i in I:
            for j in J:
                if 0 < dm[i, j] < min:
                    min = dm[i, j]
                    min_j = j
        J.remove(min_j)
        I.append(min_j)
        P.append(min_j)
    result = []
    for p in P:
        row = []
        for q in P:
            row.append(dm[p, q])
        result.append(row)
    return result


def heatmap(diss_matrix, path):
    fig, ax = plt.subplots()
    colormap = plt.cm.cubehelix_r
    ax = sns.heatmap(diss_matrix, cmap=colormap)
    fig.savefig(path)


diss_matrix = [[0, 0.255, 0.505, 0.625, 0.87],
               [0.255, 0., 0.725, 0.715, 0.435],
               [0.505, 0.725, 0., 0.785, 0.64],
               [0.625, 0.715, 0.785, 0., 0.4],
               [0.87, 0.435, 0.64, 0.4, 0.]]

ordered_diss_matrix = order(diss_matrix)
heatmap(ordered_diss_matrix, constants.CLUSTER_OUT + 'ordered_diss_heatmap')
