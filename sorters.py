def bubble_sort(x):

    n = len(x)
    while n:
        n_ = 0
        for i in range(1, n):
            if x[i - 1] > x[i]:
                x[i - 1], x[i] = x[i], x[i - 1]
                n_ = i
        n = n_
    return x


def insertion_sort(x):

    i = 1
    while i < len(x):
        j = i
        while j > 0 and x[j - 1] > x[j]:
            x[j], x[j - 1] = x[j - 1], x[j]
            j = j - 1

        i += 1

    return x


def merge_sort(x):

    result = []
    if len(x) == 1:
        return x

    left = x[: len(x) // 2]
    right = x[len(x) // 2 :]

    y = merge_sort(left)
    z = merge_sort(right)
    while len(y) > 0 or len(z) > 0:
        if len(y) and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            for i in z:
                result.append(i)
                z.pop(0)
        else:
            for i in y:
                result.append(i)
                y.pop(0)
    return result


def quicksort(x):
    if len(x) < 2:
        return x
    head, *tail = x
    less = quicksort([i for i in tail if i < head])
    more = quicksort([i for i in tail if i >= head])
    return less + [head] + more


def selection_sort(x):

    n = len(x)
    for i in range(n):
        min_x = i
        for j in range(i, n):
            if x[j] < x[min_x]:
                min_x = j

        if min_x != i:
            x[i], x[min_x] = x[min_x], x[i]

    return x
