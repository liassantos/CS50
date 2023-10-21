import pytest

from twttr import shorten

def test_upper():
    assert shorten("CASA") == "CS"

def test_other():
    assert shorten("ILHa") == "LH"

def test_lower():
    assert shorten("c4s3") == "c4s3"
