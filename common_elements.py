# find common elements in 2 arrays


def common_elements(a, b):

    a.sort()
    b.sort()
    i, j = 0, 0

    common = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            common.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return common
