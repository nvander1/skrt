from skrt.functional import compose


def test_small_compose():
    g = lambda n: n**2 + 4 + 2*n
    h = lambda n: -3*n + 2
    g_of_h = compose(g, h)

    for n in range(10):
        assert g_of_h(n) == g(h(n))

def test_large_compose():
    a = lambda n: n**3
    b = lambda n: n*2 - 3*n
    c = lambda n: -1 * n
    d = lambda n: n*n
    e = lambda n: n*(n)
    f = lambda n: 8 * n
    g = lambda n: n**2 + 4 + 2*n
    h = lambda n: -3*n + 2
    def foo(string1, string2, string3='23'):
        return sum(int(string) for string in [string1, string2, string3])

    composed = compose(a, b, c, d, e, f, g, h, foo)
    assert composed('1', '2', string3='0') == a(b(c(d(e(f(g(h(foo('1', '2', string3='0')))))))))
