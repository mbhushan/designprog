""" Given a matrix in which each row and each column is sorted,
write a method to find an element in it. """


def find_element(M, key):
    nrow = len(M)
    ncol = len(M[0])
    r = 0
    c = ncol-1
    while r < nrow and c >= 0:
        if M[r][c] == key:
            return True
        elif M[r][c] > key:
            c -= 1
        else:
            r += 1
    return False


def test_matrix():
    M = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    assert find_element(M, 10) == True
    assert find_element(M, 13) == False
    return "All Test Pass!"


def main():
    print test_matrix()

if __name__ == '__main__':
    main()
