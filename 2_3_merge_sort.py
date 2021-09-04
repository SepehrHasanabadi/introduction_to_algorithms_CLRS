import math
def merge_sort(input_list, index_orgin=0, index_end=None):
	if index_end is None:
		index_end = len(input_list) - 1
	if index_orgin < index_end:
		middle_index = int((index_orgin + index_end)/2) + 1
		merge_sort(input_list, index_orgin, middle_index - 1)
		merge_sort(input_list, middle_index, index_end)
		merge(input_list, index_orgin, middle_index, index_end)
	return input_list

def merge(input_list, index_orgin, index_middle, index_end):
	left_list = input_list[index_orgin:index_middle].copy()
	right_list = input_list[index_middle:index_end + 1].copy()
	left_list.append(math.inf)
	right_list.append(math.inf)
	sentinel_left = 0
	sentinel_right = 0
	for i in range(index_orgin, index_end + 1):
		if left_list[sentinel_left] > right_list[sentinel_right]:
			input_list[i] = right_list[sentinel_right]
			sentinel_right += 1
		else:
			input_list[i] = left_list[sentinel_left]
			sentinel_left += 1
	return input_list
