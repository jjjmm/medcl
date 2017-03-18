from k_modes import k_modes
from util import constants
from validation import fp_growth

k_modes_cluster_dict = k_modes.k_modes_dict(cluster_amount=3, data_path=constants.SORTED_MED_DATA_MIN_PATH, max_rows=150, max_columns=10)
fp_growth.fp_growth(k_modes_cluster_dict, min_support=20)

# hac
# generated_data = data_util.generate_dummy(element_amount=40, dimensions=2, seed=24)
# hac.cluster(generated_data)
# sorted_med_data = data_util.get_array_from_csv(constants.SORTED_MED_DATA_MIN_PATH)
# numeric_columns_of_sorted_med_data = np.char.decode(sorted_med_data[1:, 1:4], encoding='UTF-8')
# hac.cluster_with_dendrogram(numeric_columns_of_sorted_med_data)
