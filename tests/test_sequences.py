from skrt.utils import head, tail, init, last


def test_head():
    hello = "hello world"
    assert head(hello) == "h"


def test_tail():
    hello = "hello world"
    assert tail(hello) == "ello world"


def test_init():
    hello = "hello world"
    assert init(hello) == "hello worl"


def test_last():
    hello = "hello world"
    assert last(hello) == "d"
