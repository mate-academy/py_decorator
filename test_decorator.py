import decorator


def test_3():
    assert decorator.func(3) == 12


def test_6():
    assert decorator.func(6) == 12


def test_7():
    assert decorator.func(7) == 12
