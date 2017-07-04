from skrt.utils import rmap


def square(x):
    return x ** 2


def test_list():
    list_ = [1, 2, 3, 4, 5]
    assert rmap(list_, square, int) == [1, 4, 9, 16, 25]


def test_tuple():
    tuple_ = (1, 2, 3, 4, 5)
    assert rmap(tuple_, square, int) == (1, 4, 9, 16, 25)


def test_set():
    set_ = {1, 2, 3, 4, 5}
    assert rmap(set_, square, int) == {1, 4, 9, 16, 25}


def test_dict():
    dict_ = {'a': 1, 'b': 2, 'c': 3}
    assert rmap(dict_, square, int) == {'a': 1, 'b': 4, 'c': 9}


def test_complex_nested():
    obj = ['1', 2, ({3: 4}, {5, '6'})]
    assert rmap(obj, square, int) == ['1', 4, ({3: 16}, {'6', 25})]
