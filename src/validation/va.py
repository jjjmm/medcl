from matplotlib import pyplot as plt
import seaborn as sns
from src.util import constants, data_util
from src.validation import simple_matching
from src import hdbscan_impl
import pandas as pd


df = data_util.get_dataframe(constants.DATASETS + '2_344.csv', max_rows=1000, max_columns=300)
df.fillna(value='missing', inplace=True)
df = df.astype(str)

vals = []
cluster_dict = hdbscan_impl.hdbscan_dict(df, visualize_tree=False, log=True)
# cluster_dict = k_modes.k_modes_dict(cluster_amount=3, dataframe=df)
keys_by_cluster_size = sorted(cluster_dict, key=lambda k: len(cluster_dict[k]), reverse=True)
for key in keys_by_cluster_size:
    for el in cluster_dict.get(key):
        vals.append(el)

dm = simple_matching.get_dissimilarity_matrix(pd.DataFrame(vals))
fig, ax = plt.subplots()
colormap = plt.cm.cubehelix_r
ax = sns.heatmap(dm, cmap=colormap)
fig.savefig(constants.DATA + 'va/hdbscan/dataset_1g')

