"""This module implements specialized containers as alternatives
to Python's built-in types and to those defined in the collections
standard module.

* defaultnamedtuple  factory function for namedtuples with default arguments
* forwardingdict     subclass of default dict that passes missing key to factory

"""

import collections

def defaultnamedtuple(typename, *args, **kwargs):
    """Creates a new subclass of tuple with named fields and default arguments.

    Parameters
    ----------
    typename : str
        The name of the new type.
    args : list
        The required positional arguments for the subclass.
    kwargs : dict
        The optional arguments for the subclass.

    Returns
    -------
    subclass : `typename`
        The new subclass of tuple with fields defined by `args` and
        default fields defined by `kwargs`.

    Examples
    --------
    >>> Name = defaultnamedtuple('Name', 'last', 'first', middle=None)
    >>> Name('Doe', 'John')
    Name(last='Doe', first='John', middle=None)
    >>> Name(first='Jane', last='Doe', middle='Kim')
    Name(last='Doe', first='Jane', middle='Kim')
    >>> Name('Smith', 'John', 'Robert')
    Name(last='Smith', first='John', middle='Robert')

    """
    subclass = collections.namedtuple(typename, args + tuple(kwargs))
    subclass.__new__.__defaults__ = tuple(kwargs.values())
    kwargs_list = repr(kwargs)[1:-1].replace(': ', '=')
    arg_list = repr(args)[1:-1]
    arg_list = (arg_list + ', ' + kwargs_list).replace("'", '')
    subclass.__doc__ = f'{typename}({arg_list})'
    return subclass


class forwardingdict(collections.defaultdict):
    """A subclass of `collections.defaultdict` that passes missing key to
    factory function.

    Examples
    --------
    >>> test_dict = forwardingdict(list)
    >>> test_dict['hello']
    ['h', 'e', 'l', 'l', 'o']
    >>> test_dict = forwardingdict(lambda key: list())
    >>> test_dict['hello']
    []
    """
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            value = self[key] = self.default_factory(key)
            return value
