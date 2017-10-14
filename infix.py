
def infix_prefix(expr):

	ops = {'+':0, '-':0, '/':1, '*':1}
	operands = []
	prefix = []	
	for c in expr:
		if c in ops:
			while operands and ops[operands[-1]] >= ops[c]:
				prefix.append(operands.pop())
			operands.append(c)

		elif c != ' ':
			prefix.append(c)
	
	while operands:
		prefix = [operands.pop()] + prefix

	return ' '.join(prefix)
