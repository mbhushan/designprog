# from deal import deal_cards
from deal import deal
from poker import hand_rank


hand_names = ["Straight Flush",
              "Four of a kind",
              "Full House",
              "Flush",
              "Straight",
              "Three of a kind",
              "Two Pair",
              "Pair",
              "High Card"]

hand_names = hand_names[::-1]


def hand_percentages(n=1000000):
    """ sample n random hands and print percentages for each hand """
    counts = [0]*9
    for i in range(n/10):
        hands = deal(10)
        for hand in hands:
            rank = hand_rank(hand)[0]
            counts[rank] += 1
    for i in reversed(range(9)):
        print "%20s: %6.3f %%" % (hand_names[i], (100.*counts[i]/n))


def main():
    hand_percentages(10000000)


if __name__ == '__main__':
    main()
