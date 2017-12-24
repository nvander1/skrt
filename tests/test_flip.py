from skrt.functional import flip


def test_flip():
    f = lambda x, y: x - y
    assert flip(f)(5, 0) == f(0, 5)

    def g(*xs):
        return ''.join(xs)
    assert flip(g)('h', 'e', 'l', 'l', 'o') == 'olleh'
