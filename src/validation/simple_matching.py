def simple_matching_dissimilarity_coefficient(X, Y, dm):
    unequals_array = X != Y
    return unequals_array.sum() / X.size


def get_dissimilarity_matrix(dataframe):
    m_coefficients = []
    data_matrix = dataframe.as_matrix()
    for idx, m_row in enumerate(data_matrix):
        n_coefficients = []
        print(idx)
        for n_row in data_matrix:
            n_coefficients.append(simple_matching_dissimilarity_coefficient(m_row, n_row, data_matrix))
        m_coefficients.append(n_coefficients)
    return m_coefficients


def simple_matching_dissimilarity_coefficient_opt(X, Y):
    coefficients = []
    unequals_matrix = X != Y
    for m_row in unequals_matrix:
        coefficients.append(m_row.sum() / X.size)
    return coefficients


def get_dissimilarity_matrix_opt(dataframe):
    coefficients = []
    data_matrix = dataframe.as_matrix()
    for idx, row in enumerate(data_matrix):
        coefficients.append(simple_matching_dissimilarity_coefficient_opt(row, data_matrix))
    return coefficients
