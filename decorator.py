"""
docstring
"""


def hide(func):
    """

    :param func:
    :return:
    """
    def wrap(arg):
        """

        :param arg:
        :return:
        """
        if arg < 5:
            arg *= 2
        res = func(arg)
        return res + 1 if res % 2 else res
    return wrap


@hide
def function(arg):
    """

    :param arg:
    :return:
    """
    return arg + 5


print(function(7))
