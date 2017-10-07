# count set bits, the Brian Kernighan way

def count_bit(integer):

    count = 0

    while integer:

        integer &= integer - 1
        count += 1

    return count

n = 12345

print(count_bit(n) 
	== str(bin(n)).count('1'))

