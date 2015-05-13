# You are given two sorted arrays, A and B, and A has a large enough buffer at
# the end to hold B Write a method to merge B into A in sorted order


def merge_arrays(A, B):
    lenA = len(A)
    lenB = len(B)
    indA = lenA - lenB
    i = indA - 1
    j = lenB - 1
    k = lenA - 1
    while i >= 0 and j >= 0:
        if A[i] >= B[j]:
            A[k] = A[i]
            k -= 1
            i -= 1
        else:
            A[k] = B[j]
            k -= 1
            j -= 1
    while j >= 0:
        A[k] = B[j]
        k -= 1
        j -= 1
    print A


def main():
    A = [2, 4, 6, 8, 10, None, None, None]
    B = [1, 3, 5]
    merge_arrays(A, B)

if __name__ == '__main__':
    main()
