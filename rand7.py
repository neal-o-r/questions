import random as rand


def rand5():

    return rand.randint(0, 5)


def rand7():

    vals = list(range(1, 8)) * 3 + [0] * 4

    r = 0
    while r == 0:
        i = rand5()
        j = rand5()
        r = vals[r * 4 + j]

    return r
