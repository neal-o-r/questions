# check if one array is a rotated version of another

def naive_method(a1, a2):

	for i in range(len(a1)):
		a1 = a1[1:] + [a1[0]]
		if a1 == a2:
			return True
		
	return False


def string_method(a1, a2):

	s1 = ''.join(map(str, a1))
	s2 = ''.join(map(str, a2)) * 2
	i = 0
	n = len(s1)
	
	while i + n < len(s2):
		if s1 == s2[i:i + n]:
			return True

		i += 1

	return False




a1 = [4, 5, 6, 1, 3]
a2 = [6, 1, 3, 4, 5]

print(naive_method(a1, a2))
print(string_method(a1, a2))

