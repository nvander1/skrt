from pytest import raises

from skrt.containers import forwardingdict


def test_missingfactory():
    with raises(KeyError):
        test_dict = forwardingdict(None)
        test_dict['hello']


def test_passing():
    class Example():
        def __init__(self, key):
            self.key = key

    test_dict = forwardingdict(Example)
    result = test_dict['hello']

    assert isinstance(result, Example)
    assert result.key == 'hello'
