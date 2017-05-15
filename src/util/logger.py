from termcolor import colored


def log_k_modes_stats(k_modes_cluster_dict, title):
    print(colored(title, 'green'))
    for key, value in k_modes_cluster_dict.items():
        print('cluster {} contains {} data points'.format(str(key), len(value)))