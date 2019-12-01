"""Create a decorator for the function with one argument x
that: if x < 5 changes it on 2*x if the result is odd returns result + 1"""


def hide(function):
    """decorator custom implementation"""
    def wrapper(number):
        if number < 5:
            number *= 2
        total = function(number)
        return total + 1 if total % 2 else total
    return wrapper


@hide
def func(elem):
    """decorated method"""
    return elem + 5


print(func(7))
