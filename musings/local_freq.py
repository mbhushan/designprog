# given a string of type "AAABBCDDBBBEF"
# output: "3A2B1C2D3B1E1F"


def get_freq(st):
    result = []
    n = len(st)
    count = 0
    for i in range(n-1):
        if st[i] == st[i+1]:
            count += 1
        else:
            result.append(str(count+1))
            result.append(st[i])
            count = 0
    if st[i] == st[n-1]:
        result.append(str(count+1))
        result.append(st[i])
    else:
        result.append(str(1))
        result.append(st[n-1])
    return ''.join(result)


def main():
    st = raw_input("Enter string: ")
    op = get_freq(st)
    print "output: ", op

if __name__ == '__main__':
    main()
