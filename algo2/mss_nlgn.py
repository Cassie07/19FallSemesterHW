def find_max_subarray(arr, start, end):
    """Returns (l, r, m) such that arr[l:r] is the maximum subarray in
    A[start:end] with sum m. Here A[start:end] means all A[x] for start <= x <
    end."""
    # base case
    if start == end - 1:
        return start, end, arr[start]
    else:
        mid = (start + end)//2
        left_start, left_end, left_max = find_max_subarray(arr, start, mid)
        right_start, right_end, right_max = find_max_subarray(arr, mid, end)
        cross_start, cross_end, cross_max = find_max_crossing_subarray(arr, start, mid, end)
        if (left_max > right_max and left_max > cross_max):
            return left_start, left_end, left_max
        elif (right_max > left_max and right_max > cross_max):
            return right_start, right_end, right_max
        else:
            return cross_start, cross_end, cross_max

def find_max_crossing_subarray(arr, start, mid, end):
    """Returns (l, r, m) such that arr[l:r] is the maximum subarray within
    arr with start <= l < mid <= r < end with sum m. The arguments start, mid,
    end must satisfy start <= mid <= end."""
    sum_left = float('-inf')
    sum_temp = 0
    cross_start = mid
    for i in range(mid - 1, start - 1, -1):
        sum_temp = sum_temp + arr[i]
        if sum_temp > sum_left:
            sum_left = sum_temp
            cross_start = i

    sum_right = float('-inf')
    sum_temp = 0
    cross_end = mid + 1
    for i in range(mid, end):
        sum_temp = sum_temp + arr[i]
        if sum_temp > sum_right:
            sum_right = sum_temp
            cross_end = i + 1
    return cross_start, cross_end, sum_left + sum_right

arr = input('Enter the list of numbers: ')
arr = arr.split()
arr = [float(x) for x in arr]
start, end, maximum = find_max_subarray(arr, 0, len(arr))
print('The maximum subarray starts at index {}, ends at index {}'
      ' and has sum {}.'.format(start, end - 1, maximum))
