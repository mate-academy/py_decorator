"""
hide
"""


def hide(func):
    """

    :param func:
    :return:
    """
    def decorator(number):
        if number < 5:
            number *= 2

        res = func(number)

        if res % 2:
            res += 1

        return res

    return decorator


@hide
def add(number):
    """

    :param number:
    :return:
    """
    return number + 5


print(add(7))
