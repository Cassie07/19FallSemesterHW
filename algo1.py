# importing the required modules
%matplotlib inline
# if you run in terminal/command, please just delete this line
import matplotlib.pyplot as plt
import numpy as np
from random import randint
import time

# SelectSort
def SelectSort(arr):
	for i in range(len(arr)):
# Find the minimum element in remaining
# unsorted array
		min_idx = i
		for j in range(i+1, len(arr)):
			if arr[min_idx] > arr[j]:
				min_idx = j

	# Swap the found minimum element with
	# the first element
		arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Function to do insertion sort
def InsertSort(arr):
	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key

# MergeSort
def MergeSort(arr):
#	print(arr)
	if len(arr) >1:
		mid = len(arr)//2 #Finding the mid of the array
		L = arr[:mid] # Dividing the array elements
		R = arr[mid:] # into 2 halves

		MergeSort(L) # Sorting the first half
		MergeSort(R) # Sorting the second half

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i+=1
			else:
				arr[k] = R[j]
				j+=1
			k+=1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i+=1
			k+=1

		while j < len(R):
			arr[k] = R[j]
			j+=1
			k+=1
#	print(arr)


def average_case(i, ave_merge, ave_insert, ave_select):
    for j in range(0,10):
        mylist = [randint(0,i) for x in range(i)]
        copy = [i for i in mylist]
        since = time.time_ns()
        MergeSort(mylist)
        time_elapsed = time.time_ns() - since
        ave_merge += time_elapsed

        mylist = copy
        since = time.time_ns()
        InsertSort(mylist)
        time_elapsed = time.time_ns() - since
        ave_insert += time_elapsed

        mylist = copy
        since = time.time_ns()
        SelectSort(mylist)
        time_elapsed = time.time_ns() - since
        ave_select += time_elapsed
    ave_merge = ave_merge/10
    ave_insert = ave_insert/10
    ave_select = ave_select/10
    return ave_merge, ave_insert, ave_select

def extreme_case(i, which_case, merge, insert, select):
    if which_case == 'best_case':
        for j in range(0,10):
            mylist = [randint(0,i) for x in range(i)]
            mylist.sort(reverse= False)
            copy = [i for i in mylist]

            since = time.time_ns()
            MergeSort(mylist)
            time_elapsed = time.time_ns() - since
            merge += time_elapsed

            mylist = copy
            since = time.time_ns()
            InsertSort(mylist)
            time_elapsed = time.time_ns() - since
            insert += time_elapsed

            mylist = copy
            since = time.time_ns()
            SelectSort(mylist)
            time_elapsed = time.time_ns() - since
            select += time_elapsed
        merge = merge/10
        insert = insert/10
        select = select/10
    elif which_case == 'worst_case':
        for j in range(0,10):
            mylist = [randint(0,i) for x in range(i)]
            mylist.sort(reverse= True)
            copy = [i for i in mylist]
            since = time.time_ns()
            MergeSort(copy)
            time_elapsed = time.time_ns() - since
            merge += time_elapsed

            my_list = copy
            since = time.time_ns()
            InsertSort(mylist)
            time_elapsed = time.time_ns() - since
            insert += time_elapsed

            mylist = copy
            since = time.time_ns()
            SelectSort(mylist)
            time_elapsed = time.time_ns() - since
            select += time_elapsed
        merge = merge/10
        insert = insert/10
        select = select/10
    #print('{} time of {} : {}'.format(which_case, which_sort, times))
    return merge, insert, select

n= [i*100 for i in range(1,21)] # different input size
ave_merge = []
ave_insert = []
ave_select = []
best_merge = []
best_insert = []
best_select = []
worst_merge = []
worst_insert = []
worst_select = []

input_size = []
for i in n:
    avemerge = 0
    aveinsert = 0
    aveselect = 0
    print('The input size is : {}'.format(i))
    input_size.append(i)
    avemerge, aveinsert, aveselect = average_case(i, avemerge, aveinsert, aveselect)
    ave_merge.append(avemerge)
    ave_insert.append(aveinsert)
    ave_select.append(aveselect)

    merge = 0
    insert = 0
    select = 0
    print('The input size is : {}'.format(i))
    merge, insert, select = extreme_case(i,'best_case', merge, insert, select)
    best_merge.append(merge)
    best_insert.append(insert)
    best_select.append(select)

    merge = 0
    insert = 0
    select = 0
    print('The input size is : {}'.format(i))
    merge, insert, select = extreme_case(i,'worst_case', merge, insert, select)
    worst_merge.append(merge)
    worst_insert.append(insert)
    worst_select.append(select)



import pandas as pd

# intialise data of lists.

#merge_data = {'input_size': input_size, 'average_case': ave_merge, 'best_case': best_merge, 'worst_case': worst_merge}
#insert_data = {'input_size': input_size, 'average_case': ave_insert, 'best_case': best_insert, 'worst_case': worst_insert}
#select_data = {'input_size': input_size, 'average_case': ave_select, 'best_case': best_select, 'worst_case': worst_select}

# Create DataFrame
#merge_df = pd.DataFrame(merge_data)
#insert_df = pd.DataFrame(insert_data)
#select_df = pd.DataFrame(select_data)
# Create DataFrame
#df = pd.DataFrame(merge_df)
# Create DataFrame
#df = pd.DataFrame(insert_df)
# Create DataFrame
#df = pd.DataFrame(select_df)

# Print the output.
#print('MergeSort')
#print(merge_df)
#print('InsertSort')
#print(insert_df)
#print('SelectSort')
#print(select_df)


plt.figure()                # the first figure
#plt.xlim(1, input)
#plt.ylim(0,0.20)
#plt.xticks(np.arange(min(x), max(x), 1.0))
#plt.yticks(np.arange(min(y), max(y), 0.1))
plt.xlabel('epoch')
plt.ylabel('loss and accuracy')
#plt.grid(True)
plt.plot(input_size,ave_merge, 'r', label='merge')
plt.plot(input_size,ave_insert,'b',label='insert')
plt.plot(input_size,ave_select,'y',label='select')
plt.axis([100, input_size[len(input_size)-1], 0, best_select[len(best_select)-1]])
plt.legend()
plt.savefig('ave.tif')
plt.show()


plt.figure()                # the first figure
#plt.xlim(1, input)
#plt.ylim(0,0.20)
#plt.xticks(np.arange(min(x), max(x), 1.0))
#plt.yticks(np.arange(min(y), max(y), 0.1))
plt.xlabel('epoch')
plt.ylabel('loss and accuracy')
#plt.grid(True)
plt.plot(input_size,best_merge, 'r', label='merge')
plt.plot(input_size,best_insert,'b',label='insert')
plt.plot(input_size,best_select,'y',label='select')
plt.axis([100, input_size[len(input_size)-1], 0, best_select[len(best_select)-1]])
plt.legend()
plt.savefig('best.tif')
plt.show()


plt.figure()                # the first figure
#plt.xlim(1, input)
#plt.ylim(0,0.20)
#plt.xticks(np.arange(min(x), max(x), 1.0))
#plt.yticks(np.arange(min(y), max(y), 1e1))
plt.xlabel('epoch')
plt.ylabel('loss and accuracy')
#plt.grid(True)
plt.plot(input_size, worst_merge, 'r', label='merge')
plt.plot(input_size, worst_insert,'b',label='insert')
plt.plot(input_size, worst_select,'y',label='select')
plt.axis([100, input_size[len(input_size)-1], 0, worst_insert[len(worst_insert)-1]])
plt.legend()
plt.savefig('worst.tif')
plt.show()
