# 4 * n * n or 4n^2 (so in a general sense, O(n^2), which is polynomial)
def bubble_sort(array):
    for i in range(0, len(array)): ### N
        for j in range(0, len(array)): ## N
            if array[i] > array[j]: # 1
                temp = array[i] # 1
                array[i] = array[j] # 1
                array[j] = temp # 1

# 2n + 1, drop the one, so O(n) (linear time)
def linear_search(array, search_value):
    for i in range(0, len(array)): # n
        if array[i] == search_value: # 1
            return i # 1 ## where range of n stops 
    return None # additional 1

# 5, so O(1), (constant time)
def parallel_sum(array1, array2, index):
    if index >= len(array1): # 1
        raise Exception("index not in array1") # 1
    if index >= len(array2): # 1
        raise Exception("index not in array2") # 1
    return array1[index] + array2[index] # 1

# how to identify a log
# - while loop
# - every time you cut the problem in half, log is involved

# n = 8, times before answers were found was 8, so log2n (log(underexponent 2)8 = 2^x = 8, so x = 3) log n aka logaritmicic
def binary_search(array, search_value):
    min = 0
    max = len(array) - 1
    while min <= max: # n
        mid = (min + max) // 2
        if search_value == array[mid]:
            return mid
        elif search_value < array[mid]:
            max = mid - 1
        else:
            min = max - 1
    return None

# n + logn + 1 = n