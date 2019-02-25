

# is element n in arr
def binary_search(lst, val):
    i = len(lst) // 2
    if len(lst) is 1 and lst[i] == val:
        return True
    elif len(lst) is 1 and lst[i] != val:
        return False
    elif lst[i] > val:
        return binary_search(lst[:i], val)
    else:
        return binary_search(lst[i:], val)


# index of n in arr, doesn't gracefully exits if value doesn't exist
def binary_search_index(lst, val, offset=0):
    i = len(lst) // 2
    if lst[i] == val:
        return i + offset
    elif lst[i] > val:
        return binary_search_index(lst[:i], val)
    else:
        return binary_search_index(lst[i:], val, offset=i+offset)
