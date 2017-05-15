from src.util import data_util, constants, decorators
from src.validation import simple_matching, silhouette
from src.data_stats.duplicates import get_cramers_by_partition
from src import k_modes, hdbscan_demo

df_150 = data_util.get_dataframe(constants.DATASETS + '2_123.csv').iloc[:, :].astype(str)
df_500 = data_util.get_dataframe(constants.GENERATED_DATASETS + '123_500.csv').iloc[:, :].astype(str)
df_1000 = data_util.get_dataframe(constants.GENERATED_DATASETS + '123_1000.csv').iloc[:, :].astype(str)
df_5000 = data_util.get_dataframe(constants.GENERATED_DATASETS + '123_5000.csv').iloc[:, :].astype(str)


@decorators.measure_time
def dissimilarity_matrix_benchmark(df):
    simple_matching.get_dissimilarity_matrix_opt(df)


@decorators.measure_time
def correlation_duplicates_benchmark(df):
    get_cramers_by_partition(df)


@decorators.measure_time
def k_modes_benchmark(df):
    k_modes.k_modes_dict(cluster_amount=3, dataframe=df)


@decorators.measure_time
def hdbscan_benchmark(df):
    hdbscan_demo.hdbscan_dict(df)


@decorators.measure_time
def silhouette_benchmark(df):
    silhouette.k_modes_silhouette(df, 3)


# dissimilarity_matrix_benchmark(df_150)
# dissimilarity_matrix_benchmark(df_500)
# dissimilarity_matrix_benchmark(df_1000)
# dissimilarity_matrix_benchmark(df_5000)
#
# correlation_duplicates_benchmark(df_150)
# correlation_duplicates_benchmark(df_500)
# correlation_duplicates_benchmark(df_1000)
# correlation_duplicates_benchmark(df_5000)
#
# k_modes_benchmark(df_150)
# k_modes_benchmark(df_500)
# k_modes_benchmark(df_1000)
# k_modes_benchmark(df_5000)
#
# hdbscan_benchmark(df_150)
# hdbscan_benchmark(df_500)
# hdbscan_benchmark(df_1000)
# hdbscan_benchmark(df_5000)
#
silhouette_benchmark(df_150)
silhouette_benchmark(df_500)
silhouette_benchmark(df_1000)
silhouette_benchmark(df_5000)
