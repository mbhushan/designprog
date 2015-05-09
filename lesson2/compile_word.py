

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [('%s%s' % (10**i, d)) for (i, d) in enumerate(word[::-1])]
        return '('+'+'.join(terms) + ')'
    else:
        return word


def main():
    word = raw_input("input word: ")
    ans = compile_word(str(word))
    print "compiled word:", ans


if __name__ == '__main__':
    main()
