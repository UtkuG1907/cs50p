import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("2/2") == 100
    assert convert("33/100") == 33
    assert convert("0/100") == 0


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(33) == "33%"
    assert gauge(1) == "E"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("2/1")
