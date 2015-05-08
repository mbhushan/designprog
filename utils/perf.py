import time


def timecall(fn, *args):
    """ Call function and return elapsed time """
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1 - t0, result


def timecalls(n, fn, *args):
    """ Call fn n times with args; return min, avg, and max """
    times = [timecall(fn, *args)[0] for _ in range(n)]
    return min(times), average(times), max(times)


def average(numbers):
    return sum(numbers)/float(len(numbers))


def func(n):
    if n == 0 or n == 1:
        return 1
    return n*func(n-1)


def main():
    n = input("Enter positive number: ")
    time, result = timecall(func, n)
    print "factorial: ", result
    print "time taken: ", time
    x = input("how many experimental runs? ")
    mn, avg, mx = timecalls(x, func, n)
    print "min: %s, max: %s, avg: %s" % (mn, mx, avg)


if __name__ == '__main__':
    main()
