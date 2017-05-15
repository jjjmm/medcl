from src import cramers_v
from src.duplicates import get_columns_to_remove


def remove_by_cc_below(df, cc):
    df.fillna(value='missing', inplace=True)
    columns_over_specified_cc = cramers_v.get_column_pairs_by_cramers_coef_opt(df.iloc[:, 1:], cc, 1, True)
    return df.drop(get_columns_to_remove(columns_over_specified_cc), axis=1)
