import pytest
from working import convert


def test_noNumbrs():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_withNumbrs():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_error1():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


def test_error2():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")


def test_error3():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

