"""Python's Decorator"""


def hide(func):
    """
    The decorator for the function with one argument x that
    if x < 5 changes it on 2*x
    if the result is odd returns result + 1
    :param func: function
    :return: int
    """
    def wrapper(func_arg):
        if func_arg < 5:
            func_arg *= 2
        result = func(func_arg)
        if result % 2:
            result += 1
        return result
    return wrapper


@hide
def add_five(some_int):
    """
    Add 5
    :param some_int: int
    :return: int
    """
    return some_int + 5
