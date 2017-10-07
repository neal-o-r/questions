import timeit
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
# find pairs in an array of unique values that sum to n

# O(n^2) run time
def naive_method(arr, n):

	pairs = []
	for i, a in enumerate(arr):
		for j in arr[i+1:]:
			if a + j == n:
				pairs.append((a, j))

	return pairs

def binary_search_method(arr, n):

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

	arr.sort()
	pairs = []	
	for i in arr[:len(arr)//2]:
		comp = n - i
		if binary_search(arr, comp):
			pairs.append((i, comp))

	return pairs	


def hash_table_method(arr, n):
	
	d = {a:1 for a in arr}
	pairs = []

	for a in arr[:len(arr)//2]:
		comp = n - a
		if comp in d and a != n/2:
			pairs.append((a, comp))

	return pairs 


def time_wrapper(func, *args, **kwargs):
	def wrapped():
		return func(*args, **kwargs)
	return wrapped


if __name__ == '__main__':

	nt, bt, ht = [], [], []
	ns = [10, 50, 100, 200, 500, 1000]
	for n in ns:
		print(n)
		n_all = 0
		b_all = 0
		h_all = 0
		for i in range(10):
			arr = list(range(n))
		
			nv = time_wrapper(naive_method, arr, 10)
			bn = time_wrapper(binary_search_method, arr.copy(), 10)
			hh = time_wrapper(hash_table_method, arr, 10)
			num = 10

			n_all += timeit.timeit(nv, number=num)
			b_all += timeit.timeit(bn, number=num)
			h_all += timeit.timeit(hh, number=num)

		nt.append(n_all / 100)
		bt.append(b_all / 100)
		ht.append(h_all / 100)

	plt.plot(ns, nt, '-o', label='Naive')
	plt.plot(ns, bt, '-o', label='Binary')
	plt.plot(ns, ht, '-o', label='Hash')
	plt.legend()
	plt.show()
