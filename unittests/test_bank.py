import pytest
from bank import value

def test_hello():
    assert value("hello") == "$0"

def test_h():
    assert value("hifive world") == "$20"

def test_other():
    assert value("ohio world") == "$100"
