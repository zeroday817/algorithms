#selection_sort O(n*n)

def find_smallest(arr):
	smallest = arr[0]
	smallest_id = 0

	for i in range(len(arr)):
		if(arr[i] < smallest):
			smallest = arr[i]

	return smallest

def selection_sort(arr):
	sorted_arr = []

	for i in range(len(arr)):
		smallest = find_smallest(arr)
		sorted_arr.append(smallest)
		arr.remove(smallest)

	return sorted_arr
