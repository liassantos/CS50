from unittests import hello2

def test_argument():
    assert hello2.hello("David") == "hello, David"

def test_default():
    assert hello2.hello() == "hello, world"

