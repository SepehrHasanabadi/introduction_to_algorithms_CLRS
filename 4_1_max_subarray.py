import math

def find_max_crossing_subarray(input_list, low, mid, high):
	max_left_sum = -math.inf
	sum = 0
	max_left_index = 0
	for i in range(mid - 1, low - 1, -1):
		sum = sum + input_list[i]
		if sum > max_left_sum:
			max_left_sum = sum
			max_left_index = i

	max_right_sum = -math.inf
	sum = 0
	max_right_index = 0
	for i in range(mid, high + 1):
		sum = sum + input_list[i]
		if sum > max_right_sum:
			max_right_sum = sum
			max_right_index = i
	return (max_left_index, max_right_index, max_left_sum + max_right_sum)


def find_max_subarray(input_list, low=0, high=None):
	if high is None:
		high = len(input_list) - 1
	if low == high:
		return (low, high, input_list[low])

	mid = int((low + high)/2) + 1
	left_list = find_max_subarray(input_list, low, mid - 1)
	right_list = find_max_subarray(input_list, mid, high)
	cross_list = find_max_crossing_subarray(input_list, low, mid, high)
	
	return max([left_list, cross_list, right_list], key=lambda x: x[2])
