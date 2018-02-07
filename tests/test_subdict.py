from pytest import raises

from skrt.utils import subdict


def test_missing_key():
    with raises(KeyError):
        dict_ = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        subdict_ = subdict(['e'], dict_)


def test_subdict():
    dict_ = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    assert subdict(['a', 'c'], dict_) == {'c': 3, 'a': 1}
