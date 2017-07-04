from skrt.utils import rmap


def square(x):
    return x ** 2


def test_list():
    list_ = [1, 2, 3, 4, 5]
    assert rmap(square, list_, int) == [1, 4, 9, 16, 25]


def test_tuple():
    tuple_ = (1, 2, 3, 4, 5)
    assert rmap(square, tuple_, int) == (1, 4, 9, 16, 25)


def test_set():
    set_ = {1, 2, 3, 4, 5}
    assert rmap(square, set_, int) == {1, 4, 9, 16, 25}


def test_dict():
    dict_ = {'a': 1, 'b': 2, 'c': 3}
    assert rmap(square, dict_, int) == {'a': 1, 'b': 4, 'c': 9}


def test_complex_nested():
    obj = ['1', 2, ({3: 4}, {5, '6'})]
    assert rmap(square, obj, int) == ['1', 4, ({3: 16}, {'6', 25})]


def test_unusual_mapping():
    from collections import Counter
    c = Counter([1,2,2])
    assert rmap(square, c, int) == Counter([1,2,2,2,2])
