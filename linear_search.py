#linear search O(n)
def linear_search(list, item):
	
	for i in range(len(list)+1):

		if i == item:
			return i
