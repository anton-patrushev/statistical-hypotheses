import pandas as pd
from pandas import DataFrame

import consts
from expect import get_math_expectation_from_column
from variance import get_variance_from_column
from deviation import get_standart_deviation


def read_data():
    return pd.read_csv('./data/movement_libras.data', usecols=[consts.Y_COLUMN, consts.X_COLUMN])


def main():
    data = read_data()
    Y = DataFrame(data[consts.Y_COLUMN])
    X = DataFrame(data[consts.X_COLUMN])

    y_math_expectation = get_math_expectation_from_column(Y)
    x_math_expectation = get_math_expectation_from_column(X)

    y_variance = get_variance_from_column(Y, y_math_expectation)
    x_variance = get_variance_from_column(X, x_math_expectation)

    y_standart_deviation = get_standart_deviation(Y)
    x_standart_deviation = get_standart_deviation(X)

    return 0


main()
