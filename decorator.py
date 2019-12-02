"""docstring"""


def hide(func):
    """decorator function"""
    def wrap_hide(args):
        if args < 5:
            args = args * 2
        res = func(args)
        if res % 2 != 0:
            res = res + 1
        return res
    return wrap_hide


@hide
def plus_five(number):
    """return number + 5"""
    return number + 5


print(plus_five(7))
