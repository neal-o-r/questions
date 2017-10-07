# print the binary form of a integer

def binarise(n):

    if n == 0:
        return '0'
    else:
        return binarise(n//2) + str(n%2)


