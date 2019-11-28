import decorator


def test_3():
    assert decorator.five(3) == 12


def test_6():
    assert decorator.five(6) == 12


def test_7():
    assert decorator.five(7) == 12