lst = [1,3,4,5,6,7,9]
output = [(1,1), (3, 7), (9,9)]

def not_consec(left, right):
    if not left + 1 == right:
        return True
    return False


def solve(lst):
    output = []
    bounds = [None, None]
    for i, val in enumerate(lst):

        left = lst[(i - 1) % len(lst)]
        rght = lst[(i + 1) % len(lst)]

        if not_consec(left, val):
            bounds[0] = val

        if not_consec(val, rght):
            bounds[1] = val
            output.append(tuple(bounds))

    return output
