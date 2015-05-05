
def poker(hands):
    """ return the best hand, poker([hand,..]) => hand """
    return max(hands, key=hand_rank)


def hand_rank(hand):
    """ return a value indicating the rank of the hand """
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):     # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):        # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):     # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):   # flush
        return (5, ranks)
    elif straight(ranks):       # straight
        return (4, max(ranks))
    elif kind(3, ranks):        # three of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):       # two pairs
        return (2, two_pairs(ranks), ranks)
    elif kind(2, ranks):        # one pair
        return (1, kind(2, ranks), ranks)
    else:       # highest card
        return (0, ranks)


def card_ranks(hand):
    """ return a list of ranks - sorted by highest rank first """
    ranks = [r for r,s in cards]

    for n,r in enumerate(ranks):
        if r == 'T':
            ranks[n] = 10
        elif r == 'J':
            ranks[n] = 11
        elif r == 'Q':
            ranks[n] = 12
        elif r == 'K':
            ranks[n] = 13
        elif r == 'A':
            ranks[n] = 14
        else:
            ranks[n] = int(r)
    ranks.sort(reverse=True)
    return ranks


def test():
    """Test cases for the functions in poker program """
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    #
    # add 3 new assert statements
    # here.
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)


def main():
    print test()

if __name__ == '__main__':
    main()
