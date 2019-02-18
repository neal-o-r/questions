# rotate and array 90 degrees clockwise
# witout using any extra space


a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


def rotate(a):

    n = len(a)
    for i in range(int(n / 2)):
        for j in range(i, n - i - 1):
            temp = a[i][j]

            a[i][j] = a[j][n - 1 - i]
            a[j][n - 1 - i] = a[n - 1 - i][n - 1 - j]
            a[n - 1 - i][n - 1 - j] = a[n - 1 - j][i]
            a[n - 1 - j][i] = temp

    return a


print(a)
print(rotate(a))
