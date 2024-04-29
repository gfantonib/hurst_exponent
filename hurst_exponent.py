#!/usr/bin/env python3

import numpy as np

from source.core import run_thru_temporal_serie
from source.core import logarithmize_data
from source.core import linear_regression_to_get_hurst

# input collection for exemple.
input_1 = np.array([12, 10, 8, 6, 4, 2, 4, 6, 8, 6, 4, 2, 1, 2, 4, 6, 8, 6, 8, 10, 8, 6, 2, 4, 6, 8, 10, 10, 12, 10, 8, 4])
input_2 = np.array([12, 2, 8, 6, 4, 2, 4, 6, 8, 6, 4, 2, 1, 2, 4, 1, 8, 6, 8, 1, 8, 6, 2, 4, 6, 8, 2, 1, 12, 10, 8, 4])
input_3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
input_4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
input_5 = np.array([2, 1, 3, 3, 9, 6, 6, 3, 2, 1, 2, 8, 5, 3, 3, 10, 7, 2, 4, 9, 3, 2, 10, 7, 7, 5, 1, 2, 7, 9, 8, 4])
input_6 = np.array([1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2])
input_7 = np.array([1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1])
input_8 = np.array([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2])
input_9 = np.array([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

# main function
# Define input array to be mesured.
input = input_5
size = len(input)

range_per_stddev_array, nbr_of_data_array = run_thru_temporal_serie(input, size)
range_per_stddev_log_array, nbr_of_data_log_array = logarithmize_data(range_per_stddev_array, nbr_of_data_array)
H = linear_regression_to_get_hurst(range_per_stddev_log_array, nbr_of_data_log_array, )

print(H)
