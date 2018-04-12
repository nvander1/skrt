from collections import namedtuple

from pytest import raises

from skrt.utils import match


def setup_module():
    global Name, Alphabet
    class Name():
        first = 'a'
        middle = 'o'
        last = 'z'
    class Alphabet():
        first = 'a'
        last = 'z'


def test_missing_key():
    with raises(KeyError):
        assert match(['first', 'middle'], [Name, Alphabet])


def test_matching_fields():
    assert match(['first', 'last'], [Name, Alphabet])
