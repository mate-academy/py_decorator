"""Calculate the result according to README.md instructions"""

def hide(the_func):
    """Hide the tricky actions"""
    def wrapper(argument):
        """Check if initial argument is less than 5 and
        if the final function result is eve or odd"""
        wrapped = the_func(argument * 2 if argument < 5 else argument)
        return wrapped if (wrapped + 5) % 2 else wrapped + 1

    return wrapper


@hide
def outer_function(argument):
    """Add 5 to argument argument"""
    return argument + 5
