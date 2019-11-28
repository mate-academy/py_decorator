"""decorator module"""


def hide(function):
    """decorator"""
    def wrapped(argument):
        if argument < 5:
            argument *= 2
        result = function(argument)
        if result % 2:
            return result + 1
        return result
    return wrapped


@hide
def func(argument):
    """some function"""
    return argument + 5
