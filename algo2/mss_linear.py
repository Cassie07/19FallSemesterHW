def find_max_subarray(arr, start, end):
    """Returns (l, r, m) such that arr[l:r] is the maximum subarray in
    A[start:end] with sum m. Here A[start:end] means all A[x] for start <= x <
    end."""
    max_ending_at_i = max_seen_so_far = arr[start]
    max_left_at_i = max_left_so_far = start
    # max_right_at_i is always i + 1
    max_right_so_far = start + 1
    for i in range(start + 1, end):
        if max_ending_at_i > 0:
            max_ending_at_i += arr[i]
        else:
            max_ending_at_i = arr[i]
            max_left_at_i = i
        if max_ending_at_i > max_seen_so_far:
            max_seen_so_far = max_ending_at_i
            max_left_so_far = max_left_at_i
            max_right_so_far = i + 1
    return max_left_so_far, max_right_so_far, max_seen_so_far


arr = input('Enter the list of numbers: ')
arr = arr.split()
arr = [float(x) for x in arr]
start, end, maximum = find_max_subarray(arr, 0, len(arr))
print('The maximum subarray starts at index {}, ends at index {}'
      ' and has sum {}.'.format(start, end - 1, maximum))
