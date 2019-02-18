# reverse a given string

# do it iteratively
def reverse_string_iter(s):

    out = ""
    for i in s:
        out = i + out

    return out


# do it recursively
def reverse_recursive(s):

    if len(s) == 1:
        return s

    return reverse_recursive(s[len(s) // 2 :]) + reverse_recursive(s[: len(s) // 2])
