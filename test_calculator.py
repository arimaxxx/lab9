import pytest

from calculator import Calculator


@pytest.mark.parametrize(
    "a, b, expected",
    [(2, 3, 5), (-2, -3, -5), (-2, 2, 0), (1.5, 2.5, 4.0)],
)
def test_add(a, b, expected):
    assert Calculator().add(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a, b, expected",
    [(6, 3, 2), (-6, 3, -2), (0, 5, 0), (7, 2, 3.5)],
)
def test_divide(a, b, expected):
    assert Calculator().divide(a, b) == pytest.approx(expected)


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator().divide(10, 0)


@pytest.mark.parametrize(
    "number, expected",
    [
        (-5, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (9, False),
        (17, True),
        (25, False),
    ],
)
def test_is_prime_number(number, expected):
    assert Calculator().is_prime_number(number) is expected
