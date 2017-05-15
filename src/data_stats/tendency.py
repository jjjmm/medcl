import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from src.util import data_util, constants
from src.validation import simple_matching


def order(diss_matrix):
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
    # P.append(np.argmin(extracted_cols_rows))


df = data_util.get_dataframe(constants.DATASETS + '2_123.csv')
df.fillna(value='missing', inplace=True)
distance_matrix = simple_matching.get_dissimilarity_matrix(df.iloc[:, 1:])
distance_matrix = np.random.rand(10, 10)

b = np.random.random_integers(0, 75, size=(150, 150))
b_symm = (b + b.T) / 200
np.fill_diagonal(b_symm, 0)
print(np.matrix(b_symm))
# dm = [[0, 0.255, 0.505, 0.625, 0.87], [0.255, 0., 0.725, 0.715, 0.435], [0.505, 0.725, 0., 0.785, 0.64], [0.625, 0.715, 0.785, 0., 0.4],
#       [0.87, 0.435, 0.64, 0.4, 0.]]
print(np.matrix(b_symm))
print('================================================')
dm = order(distance_matrix)
#
print(np.matrix(dm))
fig, ax = plt.subplots()
colormap = plt.cm.cubehelix_r
ax = sns.heatmap(distance_matrix, cmap=colormap)
fig.savefig(constants.DATA + 'tendency/11_05/2_vat')


