"""
module decorator
"""
from typing import Callable, Any


def hide(function: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """
    Decorator for the function with one argument num that:
    if num < 5 changes it on 2 * num
    if the result is odd returns result + 1
    :param function: Callable[[Any], Any]
    :return: Callable[[Any], Any]
    """

    def wrapper(num):
        if num < 5:
            num *= 2
        result = function(num)
        return result + 1 if result % 2 else result

    return wrapper


@hide
def func(num: int) -> int:
    """
    Increase the number by 5.
    :param num: int
    :return: int
    """
    return num + 5


print(func(7))
