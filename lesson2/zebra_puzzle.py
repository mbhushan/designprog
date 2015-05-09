import itertools
import time
from neighbors import nextto
from neighbors import imright


def zebra_puzzle():
    houses = [first, _, middle, _, _] = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))    #1
    return next((WATER, ZEBRA)
                for(red, green, ivory, yellow, blue) in orderings
                if imright(green, ivory)    #6
                for(Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
                if Englishman is red    #2
                if Norwegian is first   #10
                if nextto(Norwegian, blue)      #15
                for(coffee, tea, milk, oj, WATER) in orderings
                if coffee is green  #4
                if Ukranian is tea  #6
                if milk is middle       #9
                for(OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Kools is yellow       #8
                if LuckyStrike is oj    #13
                if Japanese is Parliaments      #14
                for(dog, snails, fox, horse, ZEBRA) in orderings
                if Spaniard is dog      #3
                if OldGold is snails    #7
                if nextto(Chesterfields, fox)   #11
                if nextto(Kools, horse)     #12
                )

def timecall(fn, *args):
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1 - t0, result


def timecalls(n, fn, *args):
    """ Call fn n times with args; return min, avg, and max """
    if isinstance(n, int):
        times = [timecall(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times) < n:
            times.append(timecall(fn, *args)[0])
    return min(times), average(times), max(times)


def average(numbers):
    return sum(numbers)/float(len(numbers))


def main():
    time, result = timecall(zebra_puzzle)
    print result
    print "total time: ", time
    x = input("how many experimental runs? ")
    mn, avg, mx = timecalls(x, zebra_puzzle)
    print "min: %s, max: %s, avg: %s" % (mn, avg, mx)


if __name__ == '__main__':
    main()
