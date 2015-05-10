

def expand_around_center(st, i, j):
	left = i
	right = j
	while (left >= 0 and right < len(st) and st[left] == st[right]):
		left = left - 1
		right = right + 1
	return (abs(right-left-1), left+1, right)

def longest_palindrome(text):
	if text is None:
		return None
	if len(text) < 2:
		return (0, len(text))
	text = text.lower()
	result = max([max(expand_around_center(text, i,i), expand_around_center(text, i,i+1)) for i in range(len(text))])
	return (result[1], result[2])
	
def test_palindrome():
    L = longest_palindrome
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

def main():
	print test_palindrome()

if __name__ == '__main__':
	main()