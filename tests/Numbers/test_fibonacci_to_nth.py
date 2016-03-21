import pytest
from fibonacci_to_nth import fibonacci_to_nth


def test_not_int():
    with pytest.raises(TypeError):
        fibonacci_to_nth(1.2)
    with pytest.raises(TypeError):
        fibonacci_to_nth([1])
    with pytest.raises(TypeError):
        fibonacci_to_nth({})
    with pytest.raises(TypeError):
        fibonacci_to_nth(None)
    with pytest.raises(TypeError):
        fibonacci_to_nth("1")


def test_less_than_0():
    with pytest.raises(ValueError):
        fibonacci_to_nth(-1)


def test_0():
    assert fibonacci_to_nth(0) == []


def test_1():
    assert fibonacci_to_nth(1) == [0]


def test_2():
    assert fibonacci_to_nth(2) == [0, 1]


def test_3():
    assert fibonacci_to_nth(3) == [0, 1, 1]


def test_20():
    assert fibonacci_to_nth(20) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

