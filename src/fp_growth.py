import pyfpgrowth
from src.util import decorators


@decorators.measure_time
def fp_growth(k_modes_cluster_dict, min_support):
    print('\n====================================================')
    for key, value in k_modes_cluster_dict.items():
        print('cluster {} contains {} data points'.format(str(key), len(value)))
    for key, value in k_modes_cluster_dict.items():
        patterns = pyfpgrowth.find_frequent_patterns(value, min_support)
        print('\n===================fp-growth. cluster: {} with {} data points======================='.format(key, len(value)))
        for pkey, pvalue in patterns.items():
            print(str(pvalue) + ': ' + str(pkey))

