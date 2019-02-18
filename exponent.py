def exponent(x, n):

    if n == 1:
        return x

    return x * exponent(x, n - 1)


# runs in O(log n)
def exp_by_sq(x, n):

    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return exp_by_sq(x * x, n / 2)
    else:
        return exp_by_sq(x * x, (n - 1) / 2)
