import decorator


def test_3():
    assert decorator.add_five(3) == 12


def test_6():
    assert decorator.add_five(6) == 12


def test_7():
    assert decorator.add_five(7) == 12