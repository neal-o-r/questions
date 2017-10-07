

def squareroot(n):

	guess = 1
	eps = 0.00001
	
	while abs(guess * guess - n) > eps:

		guess += (n - guess*guess) / (2 * guess)

	return guess
