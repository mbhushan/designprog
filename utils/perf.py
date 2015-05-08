import time


def timecall(fn, n):
    """ Call function and return elapsed time """
    t0 = time.clock()
    fn(n)
    t1 = time.clock()
    return t1 - t0


def func(n):
    if n == 0 or n == 1:
        return 1
    return n*func(n-1)


def main():
    n = input("Enter positive number: ")
    print "factorial: ", func(n)
    print "time taken: ", timecall(func, n)


if __name__ == '__main__':
    main()
