"""
A circus is designing a tower routine consisting of people standing atop one
anothers shoulders For practical and aesthetic reasons, each person must be
both shorter and lighter than the person below him or her Given the heights and
weights of each person in the circus, write a method to compute the largest
possible number of peo- ple in such a tower
EXAMPLE:
    Input (ht, wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68, 110)
    Output: The longest tower is length 6 and includes from top to bottom:
        (56, 90) (60,95) (65,100) (68,110) (70,150) (75,190)
"""


def circus_design(people_list):
    print sorted(people_list, key=lambda x: x[0])


def main():
    people_list = [(65, 92), (70, 150), (56, 90),
                   (75, 190), (60, 95), (68, 110)]
    circus_design(people_list)

if __name__ == '__main__':
    main()
