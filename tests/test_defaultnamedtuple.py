from pytest import raises

from skrt.containers import defaultnamedtuple


Name = defaultnamedtuple('Name', 'first', 'last', middle='', prefix='Mr.')


def test_positional_arg_assignment():
    john_doe = Name('John', 'Doe')
    assert john_doe.first == 'John'
    assert john_doe.last == 'Doe'


def test_missing_positional_args():
    with raises(TypeError):
        john = Name('John')


def test_kwarg_default():
    mr_john_doe = Name('John', 'Doe')
    assert mr_john_doe.middle == ''
    assert mr_john_doe.prefix == 'Mr.'


def test_kwarg_assign():
    dr_john_doe = Name('John', 'Doe', prefix='Dr.')
    assert dr_john_doe.prefix == 'Dr.'


def test_repr():
    john_doe = Name('John', 'Doe', middle='M')
    assert repr(john_doe) == ("Name(first='John', last='Doe', "
                              "middle='M', prefix='Mr.')")
