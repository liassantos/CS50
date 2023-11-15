import pytest
from numb3rs import validate


def test_true1():
    assert validate("127.0.0.1") == True


def test_true2():
    assert validate("255.255.255.255") == True


def test_false1():
    assert validate("512.512.512.512") == False


def test_false2():
    assert validate("1.2.3.1000") == False


def test_notnumber():
    assert validate("cat") == False


def test_range():
    assert validate("75.456.76.65") == False

