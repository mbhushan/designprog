from functools import update_wrapper

#def decorator(d):
#    """ make function d a decorator, d wraps a function fn """
#    def _d(fn):
#        return update_wrapper(d(fn), fn)
#    update_wrapper(_d, d)
#    return _d


# does this work?
def decorator(d):
    """make function d a decorator, d wraps a function fn """
    return lambda fn: update_wrapper(d(fn), fn)


decorator = decorator(decorator)
print decorator
