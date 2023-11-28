import pytest
from um import count

def test_only_um():
    assert count("um") == 1


def test_um_with_symbol():
    assert count("um?") == 1


def test_um_upper_one_time():
    assert count("Um, thanks for the album.") == 1


def test_um_several_times():
    assert count("Um, thanks, um...") == 2
