import random


def shuffle_1(deck):
    """ Wrong shuffling strategy """
    N = len(deck)
    swapped = [False]*N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = swapped[j] = True
        swap(deck, i, j)
    return deck


def swap(deck, i, j):
    """ swap element i and j of collection deck """
    # print "swap: ", i, j
    deck[i], deck[j] = deck[j], deck[i]


def main():
    deck = [r+s for r in "23456789TJQKA" for s in "SHDC"]
    print "Wrong Shuffling Procedure: "
    print shuffle_1(deck)


if __name__ == '__main__':
    main()
