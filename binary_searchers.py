

# is element n in arr
def binary_search(arr, n):

	pivot = arr[len(arr)//2]
	if pivot == n:
		return True
	if len(arr) == 1:
		return False

	if pivot > n:
		return binary_search(arr[:len(arr)//2], n)
	else:
		return binary_search(arr[len(arr)//2:], n)


# index of n in arr
def binary_search_index(arr, n, i=0):

	pivot = arr[len(arr)//2]
	if pivot == n:
		return i + len(arr)//2
	if len(arr) == 1:
		return False

	if pivot > n:
		return binary_search_index(arr[:len(arr)//2], n, i)
	else:
		i += len(arr)//2
		return binary_search_index(arr[len(arr)//2:], n, i)



