import string, re

def valid(f):
    "Formula f is valid iff it has no numbers with leading zero and evals true."
    table = string.maketrans("ABC", "123")
    try:
    	expr = eval(f.translate(table)) 
    	print "Expr: ", expr
        return not re.search(r'\b0[0-9]', f) and eval(f.translate(table)) is True
    except ZeroDivisionError:
        return False

def main():
	f = "A+B==C"
	print valid(f)

if __name__ == '__main__':
	main()
