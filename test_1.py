import pytest


def sum_digits(N):
    return sum(range(1, N + 1))


def test_positive():
    assert sum_digits(1000)


def test_null():
    assert sum_digits(0)


def test_negative():
    assert sum_digits(-1000)


def test_text():
    assert sum_digits('1000')
