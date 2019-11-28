"""docstring"""


def hide(func):
    """
    decorator
    :param func:
    :return:
    """
    def wrapper(arg):
        if arg < 5:
            arg *= 2
        res = func(arg)
        return res + 1 if res % 2 else res
    return wrapper


@hide
def add_five(arg):
    """
    Adds 5 to the x
    :param arg: int
    :return: int
    """
    return arg + 5
