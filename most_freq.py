# find most frequent number in an array


def most_frequent(arr):

    count = 1
    popular = arr[0]
    temp = 0

    for i in range(len(arr)):

        temp = arr[i]
        tempCount = 0
        for j in range(len(arr)):

            if temp == arr[j]:
                tempCount += 1

        if tempCount > count:
            popular = temp
            count = tempCount

        return popular


arr = [1, 2, 3, 1, 1]
print(most_frequent(arr) == 1)
