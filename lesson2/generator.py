

def ints(start, end):
    i = start
    while i <= end:
        yield i
        i = i + 1


def generate():
    L = ints(1, 10000)
    for i in L:
        print "%s " % (i)


def main():
    generate()


if __name__ == '__main__':
    main()
