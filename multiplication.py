# multiply 2 numbers without *


def multiply(x, y):

	if y == 1:
		return x
	
	return x + multiply(x, y-1)

