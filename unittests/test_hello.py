from hello2 import hello

def test_argument():
    assert hello2.hello("David") == "hello, David"

def test_default():
    assert hello2.hello() == "hello, world"

