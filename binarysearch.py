def binary_search(lst, value):
    '''a binary search'''

    low = 0
    high = len(lst)

    while high > low:
        mid = (high + low) // 2
        if lst[mid] == value:
            return mid
        elif lst[mid] < value:
            low = mid + 1
        else:
            high = mid
    return -1