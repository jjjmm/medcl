from src import k_modes, fp_growth
from src.util import constants, data_util

df_with_ids = data_util.get_dataframe(constants.SORTED_MED_DATA_MIN_PATH, 150, 10)
df_no_ids = df_with_ids.iloc[:, 2:]

k_modes_cluster_dict = k_modes.k_modes_dict(cluster_amount=3, dataframe=df_no_ids)
k_modes.log_k_modes_dict(k_modes_cluster_dict)

fp_growth_patterns = fp_growth.fp_growth_as_dict(k_modes_cluster_dict, min_support=20)
fp_growth.log_fp_growth_dict(fp_growth_patterns)
