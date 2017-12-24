from operator import add, sub

from skrt.functional import foldl, foldr


def test_foldl_sub():
    result = foldl(sub, 0, [1, 2, 3, 4, 5])
    assert result == -15


def test_foldl_add():
    test_list = ['h', 'e', 'l', 'l', 'o']
    result = foldl(add, '', test_list)
    assert result == ''.join(test_list)


def test_foldr_sub():
    result = foldr(sub, 0, [1, 2, 3, 4, 5])
    assert result == 3
