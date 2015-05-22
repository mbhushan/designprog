

def grammar(description):
    """ convert a description to grammar """
    G = {}
    for line in split(description, "\n"):
        lhs, rhs = split(line, " => ", 1)
        alternatives = split(rhs, " | ")
        G[lhs] = tuple(map(split, alternatives))
    return G


def split(text, sep=None, maxsplit=-1):
    """ like str.split but strips whitespaces from each split token """
    return [t.strip() for t in text.strip().split(sep, maxsplit) if t]


def main():
    description = "goal => expr \
        expr => term | term - expr \
        term => fact | fact * term \
        fact => a | b | c "
    print "Description: ", description
    print grammar(description)

if __name__ == '__main__':
    main()
