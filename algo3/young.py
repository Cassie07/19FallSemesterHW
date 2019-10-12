import sys
import numpy as np

def Young(Y, i, j, m, n):
	x = i
	y = j
	if i < m and Y[i][j] > Y[i + 1][j]:
		x = i + 1
		y = j

	if j < n and Y[x][y] > Y[i][j + 1]:
		x = i
		y = j + 1

	if x != i or y != j:
		Y[i][j], Y[x][y] = Y[x][y], Y[i][j]
		Young(Y, x, y, m, n)

def Inverse(Y, m, n):
	i = m
	j = n
	if m>0 and Y[m][n] < Y[m-1][n]:
		i = m - 1
		j = n

	if n>0 and Y[i][j] < Y[m][n-1]:
		i = m
		j = n - 1

	if i!=m or j!=n:
		Y[m][n], Y[i][j] = Y[i][j], Y[m][n]
		Inverse(Y, i, j)

def Insert(Y, m, n, value):
	if m < 0 and n < 0:
		return
	Y[m][n] = value
	Inverse(Y, m, n)

def ExtractMin(Y, m, n):
	temp = Y[0][0]
	Y[0][0] = sys.maxsize
	Young(Y, 0, 0, m, n)
	return temp

def sort(Y, m, n):
	result = []
	x = ExtractMin(Y,m,n)
	while x != sys.maxsize:
		result.append(x)
		x = ExtractMin(Y,m,n)
	return result

def YoungSearch(Y, i, j, m, n, value):
	if Y[i][j] == value:
		return True
	x = i
	y = j
	if i > 0 and Y[i][j] > value:
		x = i - 1
		y = j

	if j < n and Y[i][j] < value:
		x = i
		y = j + 1

	if x==i and y==j:
		return False


	return YoungSearch(Y,x,y,m,n,value)

def search(Y, m, n, value):
	return YoungSearch(Y, m, 0, m, n, value)

def CustomizedPrint(Y):
	for i in Y:
		for j in i:
			print("%10s"%(str(j) if j != sys.maxsize else "INF"), end="  ")
		print('')

def BuildTableaus(x, m, n):
	Y = np.ones((m,n),dtype="int64")*sys.maxsize
	for i in x:
		Insert(Y, m-1, n-1, i)
	return Y


if __name__ == '__main__':
	x = [9,16,3,2,4,8,5,14,12]
	m = 4
	n = 4

	Y = BuildTableaus(x, m, n)
	# Extract min
	print("ExtractMin")
	print("Young tableaus:")
	CustomizedPrint(Y)
	r = ExtractMin(Y, m - 1, n - 1)
	print("Minimum number be extracted: ", r)
	print("Maintain Young tableaus:")
	CustomizedPrint(Y)
	print()
	print()

	# insert
	Y = BuildTableaus(x, m, n)
	print("insert value to build Young tableaus")
	print("Young tableaus after inserting values")
	CustomizedPrint(Y)
	print()
	print()

	# Sort
	Y = BuildTableaus(x, m, n)
	print("Sorting")
	result = sort(Y, m-1, n-1)
	print("previous list is:")
	print(x)
	print("Sorted list is:")
	print(result)
	print()
	print()

	# search
	Y = BuildTableaus(x, m, n)
	print("Searching")
	print("array is:")
	print(x)
	print("Search number: 3  search result: ",search(Y, m-1, n-1, 3))
	print("Search number: 50  search result: ",search(Y, m-1, n-1, 50))
	print()
	print()
