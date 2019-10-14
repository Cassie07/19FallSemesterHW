import random
from random import randint
import time
from statistics import mean

class Interval():
	def __init__(self, start, end):
		self.start = start
		self.end = end

	@classmethod
	def copy(cls, i):
		return cls(i.start, i.end)

	def __repr__(self):
		return "("+str(self.start)+", "+str(self.end)+")"

def _build_A(l):
	A = []
	for i in l:
		interval = Interval(i[0],i[1])
		A.append(interval)
	return A

def _swap(A, i, j):
	A[i], A[j] = A[j], A[i]

############################################################################################################################
# Fuzzy-sort

def find_overlap(A, p, s):
	a = random.randint(p,s)
	_swap(A, a, s)
	interval = Interval.copy(A[s])
	for i in range(p, s):
		if not ((A[i].start > interval.end) or (A[i].end < interval.start)):
			if A[i].start > interval.start:
				interval.start = A[i].start
			if A[i].end < interval.end:
				interval.end = A[i].end

	return interval

def partition_right(A, interval, p, s):
	x = p - 1
	for i in range(p, s):
		if A[i].start <= interval.start:
			x += 1
			_swap(A, x, i)
	_swap(A, x+1, s)
	return x+1

def partition_left_middle(A, interval, p, r):
	x = p - 1
	for i in range(p, r):
		if A[i].end < interval.end:
			x += 1
			_swap(A, x, i)
	_swap(A, x+1, r)
	return x+1

def fuzzy_sort(A, p, s):
	if p < s:
		interval = find_overlap(A, p, s)
		r = partition_right(A, interval, p, s)
		q = partition_left_middle(A, interval, p, r)
		fuzzy_sort(A, p, q-1)
		fuzzy_sort(A, r+1, s)

##############################################################################################################################
# quick_sort

def QuickSort(A):
	QuickSort_internal(A, 0, len(A) - 1)

def QuickSort_internal(A, p, r):
	if p < r:
		k = randomized_partition(A, p, r)
		QuickSort_internal(A, p, k - 1)
		QuickSort_internal(A, k + 1, r)

def randomized_partition(A, p, r):
	i = randint(p, r)
	_swap(A, r, i)
	return partition(A, p, r)

def partition(A, p, r):
	x = A[r]
	i = p
	k = p
	for j in range(p, r):
		if A[j].start < x.start:
			_swap(A, i, j)
			i += 1
		elif A[j].start == x.start:
			if A[j].end < x.end:
				_swap(A, i, j)
				i += 1
	_swap(A, i, r)
	return i

############################################################################################################################
# test

def test_case1(l):
	A = _build_A(l)
	fuzzy_sort(A, 0, len(A)-1)
	return A

def test_case2(l):
	A = _build_A(l)
	fuzzy_sort(A, 0, len(A)-1)
	return A


def test_quick_sort_1(l):
	A = _build_A(l)
	QuickSort(A)
	return A

def test_quick_sort_2(l):
	A = _build_A(l)
	QuickSort(A)
	return A

###########################################################################################################################

if __name__ == '__main__':
	l1 = [(5,7), (1,3), (4,6), (8,10)]
	l2 = [(6,7),(9,11),(13,14),(3,7),(11,15),(13,14),(12,14),(14,15),(9,15),(5,7),(7,9),(1,5),(1,9),(6,10)]
	f1 = []
	f2 = []
	f3 = []
	f4 = []
	for i in range(0,5000):
		since = time.time()
		A1 = test_case1(l1)
		time_elapsed = time.time() - since
		f1.append(time_elapsed)

		since = time.time()
		A2 = test_case2(l2)
		time_elapsed = time.time() - since
		f2.append(time_elapsed)

		since = time.time()
		A3 = test_quick_sort_1(l1)
		time_elapsed = time.time() - since
		f3.append(time_elapsed)

		since = time.time()
		A4 = test_quick_sort_2(l2)
		time_elapsed = time.time() - since
		f4.append(time_elapsed)

	ave1 = mean(f1)
	ave2 = mean(f2)
	ave3 = mean(f3)
	ave4 = mean(f4)

	print("*" * 50 + "  FuzzySort: TestCase 1  " + "*" * 50)
	print("Before the sorting:")
	print(l1)
	print()
	print("After the sorting:")
	print(A1)
	print()
	print('Running time : {} ns'.format(ave1*1e9))
	print()
	print()

	print("*" * 50 + "  FuzzySort: TestCase 2  " + "*" * 50)
	print("Before the sorting:")
	print(l2)
	print()
	print("After the sorting:")
	print(A2)
	print()
	print('Running time : {} ns'.format(ave2*1e9))
	print()
	print()

	print("*" * 50 + "  QuickSort: TestCase 1  " + "*" * 50)
	print("Before the sorting:")
	print(l1)
	print()
	print("After the sorting:")
	print(A3)
	print()
	print('Running time : {} ns'.format(ave3*1e9))
	print()
	print()

	print("*" * 50 + "  QuickSort: TestCase 2  " + "*" * 50)
	print("Before the sorting:")
	print(l2)
	print()
	print("After the sorting:")
	print(A4)
	print()
	print('Running time : {} ns'.format(ave4*1e9))
	print()
