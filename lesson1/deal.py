import random


def deal(numhands, n=5, deck=[r+s for r in "23456789TJQKA" for s in "SHDC"]):
    """ shuffle the deck and deal out numhands n-cards """
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]


def deal_cards(numhands, n=5,
               deck=[r+s for r in "23456789TJQKA" for s in "SHDC"]):
    random.shuffle(deck)
    start = 0
    end = n
    result = []
    while (numhands > 0) and (end < len(deck)):
        result.append(deck[start:end])
        start += n
        end += n
        numhands -= 1
    # print result
    return result


def main():
    mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
    hands = deal_cards(7, 5, mydeck)
    print hands

if __name__ == '__main__':
    main()
