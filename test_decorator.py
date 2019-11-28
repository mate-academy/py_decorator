import decorator


def test_3():
    assert decorator.f(3) == 12


def test_6():
    assert decorator.f(6) == 12


def test_7():
    assert decorator.f(7) == 12