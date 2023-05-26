import mymath as mm


def test_add():
    assert mm.add(2, 3) == 2 + 3
    assert mm.add(5, -10.5) == 5 + (-10.5)


def test_subtract():
    assert mm.subtract(10, 5) == 10 - 5
