from functools import update_wrapper


def decorator(d):
    """ make function d a decorator, d wraps a function fn """
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d


@decorator
def memo(f):
    """Decorator that caches return value of each call to f(args).
    Then when called with some args, we can just look it up """
    cache = {}

    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some elements of args cant be a dict
            return f(args)
    return _f


callcounts = {}


@decorator
def countcalls(f):
    """decorator that counts the function calls, in callcounts[f] """
    def _f(*args):
        callcounts[_f] += 1
        return f(*args)
    callcounts[_f] = 0
    return _f


@countcalls
@memo
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print fib(11)
