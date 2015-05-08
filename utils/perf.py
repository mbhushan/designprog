import time


def timecall(fn, *args):
    """ Call function and return elapsed time """
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1 - t0, result


def func(n):
    if n == 0 or n == 1:
        return 1
    return n*func(n-1)


def main():
    n = input("Enter positive number: ")
    time, result = timecall(func, n)
    print "factorial: ", result
    print "time taken: ", time


if __name__ == '__main__':
    main()
