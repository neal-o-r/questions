# find the only unique element in an array

# in a sorted array
def unique_sorted(arr):
    x = arr[0]
    for i, a in enumerate(arr[1:]):
        if x != a and a != arr[i + 1]:
            return a
        x = a

    return x


# given that everything else appears twice
def find_double(arr):

    x = arr[0]
    for a in arr[1:]:
        x ^= a

    return x


# given that everything else appears three times
def find_triple(arr):

    one = 0
    two = 0

    for a in arr:
        two |= one & a
        one ^= a
        both = ~(one & two)
        one &= both
        two &= both

    return one
