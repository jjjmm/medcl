def simple_matching_dissimilarity_coefficient(X, Y):
    if X.size != Y.size:
        raise ValueError('compared row should be equal size')
    else:
        unequals_array = X != Y
        return unequals_array.sum() / X.size


def get_dissimilarity_matrix(dataframe):
    m_coefficients = []
    data_matrix = dataframe.as_matrix()
    for m_row in data_matrix:
        n_coefficients = []
        for n_row in data_matrix:
            n_coefficients.append(simple_matching_dissimilarity_coefficient(m_row, n_row))
        m_coefficients.append(n_coefficients)
    return m_coefficients
