# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Your code here.
    if word.isalpha() and word.islower():
        return word
    if not word.isalpha():
        return word
    result = []
    mul = 1
    word = word[::-1]
    for w in word:
        if w.isalpha and w.isupper():
            result.append(str(mul) + '*' + w + "+")
        else:
            result.append(w)
        mul = mul*10
    ans = ''.join(result)
    return ans[:-1]

def main():
    word = "YOU"
    ans = compile_word(word)
    print ans

if __name__ == '__main__':
    main()