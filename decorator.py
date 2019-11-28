"""docstring"""


def hide(funct):
    """decoration"""
    def wrapper(val):
        if val < 5:
            val *= 2
        result = funct(val)
        if result % 2:
            result += 1
        return result
    return wrapper


@hide
def func(val):
    """docstring"""
    return val + 5
