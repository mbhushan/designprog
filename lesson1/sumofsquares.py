

def func_sumofsquares(num):
    return sum([x**2 for x in range(num+1)])


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
    print "Functional style result: ", func_sumofsquares(num)


if __name__ == '__main__':
    main()
