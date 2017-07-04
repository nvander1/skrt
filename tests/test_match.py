from collections import namedtuple

from nose.tools import raises

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


@raises(KeyError)
def test_missing_key():
    assert match(['first', 'middle'], [Name, Alphabet])


def test_matching_fields():
    assert match(['first', 'last'], [Name, Alphabet])
