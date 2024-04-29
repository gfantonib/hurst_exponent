import numpy as np

# Use cutted data array to calculate the range_per_stddev.
def calculate_range_per_stddev(cutted_data_array):
	mean = np.mean(cutted_data_array)
	size = len(cutted_data_array)
	diff_accum_mean_array = np.array([])
	diff_accum_mean_curr = 0
	i = 0
	while i < size:
		diff_accum_mean_curr = diff_accum_mean_curr + (cutted_data_array[i] - mean)
		diff_accum_mean_array = np.append(diff_accum_mean_array, diff_accum_mean_curr)
		i = i + 1
	stddev = np.std(cutted_data_array)
	range = diff_accum_mean_array.max() - diff_accum_mean_array.min()
	range_per_stddev = range / stddev
	return range_per_stddev

	# Cut part of the intire input and send each cutted part to be processed 
	# by calculate_range_per_stddev function.
def run_thru_temporal_serie(input, size):
	range_per_stddev_array = np.array([])
	nbr_of_data_array = np.array([])
	i = 2
	while i <= size:
		cutted_data_array = input[0:i]
		range_per_stddev = calculate_range_per_stddev(cutted_data_array)
		range_per_stddev_array = np.append(range_per_stddev_array, range_per_stddev)
		nbr_of_data_array = np.append(nbr_of_data_array, i)
		i = i + 2
	return range_per_stddev_array, nbr_of_data_array

# Use log2 in the  arrays to build a graphic (entropic line).
def logarithmize_data(range_per_stddev_array, nbr_of_data_array):
	range_per_stddev_log_array = np.log2(range_per_stddev_array)
	nbr_of_data_log_array = np.log2(nbr_of_data_array)
	return range_per_stddev_log_array, nbr_of_data_log_array

# Calculate the line that best represent the matching points (linear regression).
# If y = mx + b, the Hurst exponet is equal to m.
# H = m.
def linear_regression_to_get_hurst(range_per_stddev_log_array, nbr_of_data_log_array):
	x = nbr_of_data_log_array
	y =  range_per_stddev_log_array
	A = np.vstack([x, np.ones(len(x))]).T
	m, b = np.linalg.lstsq(A, y, rcond=None)[0]
	H = m
	return H