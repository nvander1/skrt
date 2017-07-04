from skrt.utils import rmap


def test_list():
    list_ = [1, 2, 3, 4, 5]
    assert rmap(list_, lambda x: x**2, int) == [1, 4, 9, 16, 25]


def test_tuple():
    tuple_ = (1, 2, 3, 4, 5)
    assert rmap(tuple_, lambda x: x**2, int) == (1, 4, 9, 16, 25)


def test_set():
    set_ = {1, 2, 3, 4, 5}
    assert rmap(set_, lambda x: x**2, int) == {1, 4, 9, 16, 25}


def test_dict():
    dict_ = {'a': 1, 'b': 2, 'c': 3}
    assert rmap(dict_, lambda x: x**2, int) == {'a': 1, 'b': 4, 'c': 9}
