import decorator


def test_3():
    assert decorator.outer_function(3) == 12


def test_6():
    assert decorator.outer_function(6) == 12


def test_7():
    assert decorator.outer_function(7) == 12