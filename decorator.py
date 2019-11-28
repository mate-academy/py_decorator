"""decorator module"""


def hide(function):
    """decorator"""
    def wrapped(arg):
        if arg < 5:
            arg *= 2
        result = function(arg)
        return result + 1 if result % 2 else result
    return wrapped


@hide
def func(argument):
    """some function"""
    return argument + 5
