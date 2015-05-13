#
# Write a function, n_ary(f), that takes a binary function (a function
# that takes 2 inputs) as input and returns an n_ary function. 

def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        return x if not args else f(x, n_ary_f(*args)) 
    return n_ary_f


def func(x, y):
	return x**2 + y**2

def main():
	nfunc = n_ary(func)
	x = y = z = u = 2
	ans = nfunc(x, y, z, u)
	print "ans: ", ans

if __name__ == '__main__':
	main()