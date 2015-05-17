# decorator for tracing a function - template

@decorator
def trace(f):
    indent = '    '
    def _f(*args):
        signature = '%s(%s)' % (f.__name__, ', '.join(map(repr, args)))
        print '%s--> %s' % (trace.level * indent, signature)
        trace.level += 1
        try:
            print "%s<---%s === %s" % ((trace.level-1)*indent, signature,
                                       result)
        finally:
            pass
        return
    trace.level = 0
    return _f
