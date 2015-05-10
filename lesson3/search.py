def search(pattern, text):
    """Return true if pattern appears anywhere in text
       Please fill in the match(          , text) below.
       For example, match(your_code_here, text)"""
    if pattern.startswith('^'):
        return match( pattern[1:], text) # fill this line
    else:
        return match(  '.*' + pattern , text)


def match(pattern, text):
    """
    Return True if pattern appears at the start of text
    
    For this quiz, please fill in the return values for:
        1) if pattern == '':
       	2) elif pattern == '$':
	"""

    if pattern == '':
        return True
    elif pattern == '$':
        return text == ''
    elif len(pattern) > 1 and pattern[1] in '*?':
    	return True
    else:
        return True