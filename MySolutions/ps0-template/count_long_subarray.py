def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    ##################
    # YOUR CODE HERE #
    n = len(A)
    temp_len = 1  # record the length of current subarray
    length = 1  # record the longest length of increasing subarrays
    for i in range(1, n):
        if A[i - 1] < A[i]:
            temp_len += 1
        else:
            temp_len = 1
        if temp_len == length:
            count += 1
        elif temp_len > length:
            count = 1  # update the number
            length = temp_len  # store the longest len
    ##################
    return count
