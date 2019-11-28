def hide(f):

    return lambda x: 42


@hide
def f(x):
    return x + 5


print(f(7))