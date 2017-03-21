import pyfpgrowth
from src.util import decorators
from termcolor import colored


@decorators.measure_time
def fp_growth_as_dict(k_modes_cluster_dict, min_support):
    patterns = {}
    for key, value in k_modes_cluster_dict.items():
        patterns[key] = (pyfpgrowth.find_frequent_patterns(value, min_support))
    return patterns


def log_fp_growth_dict(patterns):
    for cluster_id, value_frequency_dict in patterns.items():
        print(colored('fp-growth. cluster: {}'.format(cluster_id), 'green'))
        for value, frequency in value_frequency_dict.items():
            print(str(value) + ' ' + str(frequency))
