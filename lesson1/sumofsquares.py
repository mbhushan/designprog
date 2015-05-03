

def calc_sumofsquares(num):
    if not isinstance(num, (int, long)):
        return None
    result = 0
    for i in range(num+1):
        result += (i*i)
    return result


def main():
    num = input("Enter number: ")
    ans = calc_sumofsquares(num)
    print "Sum of Squares: ", ans


if __name__ == '__main__':
    main()
