lst = [1,3,4,5,6,7,9]
output = [(1,1), (3, 7), (9,9)]

def is_left(left, val):
    if not left + 1 == val:
        return True
    return False

def is_right(val, right):
    if not right - 1 == val:
        return True
    return False

def solve(lst):
    output = []
    bounds = [None, None]
    for i, val in enumerate(lst):

        left = lst[(i - 1) % len(lst)]
        rght = lst[(i + 1) % len(lst)]

        if is_left(left, val):
            bounds[0] = val

        if is_right(val, rght):
            bounds[1] = val
            output.append(tuple(bounds))

    return output
