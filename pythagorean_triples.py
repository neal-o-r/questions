import math

def is_triplet(arr):

        n = len(arr)
        arr1 = arr.copy()
        for i in range(n):
                arr[i] = arr[i] * arr[i]
        
        arr.sort()
        for i in range(n-1, 1, -1):
                j = 0
                k = i - 1
                while (j < k):
                        if arr[j] + arr[k] == arr[i]:
                                return True
                        else:
                                if arr[j] + arr[k] < arr[i]:
                                        j += 1
                                else:
                                        k -= 1

        return False

def pythagoreanTriplet(n):

        for b in range(n):
                for a in range(1, b):
                        c = math.sqrt( a * a + b * b)
                if c % 1 == 0:
                        print (a, b, int(c))
