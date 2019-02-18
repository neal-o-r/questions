import random as rd

a = [rd.randint(0, 1) for i in range(200)]


def sum1s(l):
    c = 0
    for i in l:
        c += i

    return c


# this is actually slower, the bin to dec conversion
# takes longer than you gain from the faster loop
def sum1s_kernighan(l):

    n = int("".join(map(str, a)), 2)
    c = 0
    while n:
        n &= n - 1
        c += 1

    return c
