
# a stack
class Stack(object):
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data += [val]

    def pop(self):
        return self.data.pop()

    def length(self):
        return len(self.data)


def balanced_parens(exp):

    s = Stack()
    for c in exp:
        if c == "(":
            s.push(c)
        if c == ")":
            try:
                a = s.pop()
                if a != "(":
                    return False
            except:
                return False

    if s.length() > 0:
        return False
    else:
        return True


exp = "()()()"
print(balanced_parens(exp))
