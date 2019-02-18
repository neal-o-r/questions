def pair_parens(opener, closer=0, s=""):

    if opener == 0 and closer == 0:
        print(s)

    if opener > 0:
        pair_parens(opener - 1, closer + 1, s + "(")
    if closer > 0:
        pair_parens(opener, closer - 1, s + ")")
