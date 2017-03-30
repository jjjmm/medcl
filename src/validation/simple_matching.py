def simple_matching_coefficient(X, Y):
    if X.size != Y.size:
        raise ValueError('compared row should be equal size')
    else:
        equality_series = X == Y
        return equality_series.sum() / X.size

