def fib_iter(n):

    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])

    return fib


def fib_recur(n_range):
    def fib(n):
        if n < 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    return list(map(fib, range(n_range)))


table = {1: 1, 2: 1}


def fib_dynam(n):

    if n < 2:
        return 1
    if n in table:
        return table[n]

    else:
        table[n] = fib_dynam(n - 1) + fib_dynam(n - 2)
        return table[n]
