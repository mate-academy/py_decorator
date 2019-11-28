"""
Create a decorator for the function with one argument x
"""


def hide(func):
    """Func"""
    def wrapper(value):
        if value < 5:
            value *= 2
        result = func(value)
        if result % 2:
            result += 1
        return result
    return wrapper


@hide
def five(x):
    return x + 5
