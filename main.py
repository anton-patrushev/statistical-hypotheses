import pandas as pd
from pandas import DataFrame

import consts


def read_data():
    return pd.read_csv('./data/movement_libras.data',
                       usecols=[consts.result_column, consts.dependency_one_column, consts.dependency_two_column])


def main():
    data = read_data()
    Y = DataFrame(data[consts.Y_COLUMN])
    X = DataFrame(data[consts.X_COLUMN])

    return 0


main()
