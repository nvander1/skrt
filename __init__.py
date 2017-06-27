"""
This module implements nifty things I want.
"""


import collections


__all__ = ['defaultnamedtuple']


def defaultnamedtuple(typename, *args, **kwargs):
    """
    Creates a new subclass of tuple with named fields that supports optionals.

    Parameters
    ----------
    typename : str
      The name of the new type.
    args : list
      The required positional arguments for the subclass.
    kwargs : dict
      The optional arguments for the subclass.

    >>> Name = defaultnamedtuple('Name', 'last', 'first', middle=None)
    >>> Name.__doc__
    'Name(last, first, middle=None)'
    >>> Name('Doe')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: __new__() missing 1 required positional argument: 'first'
    >>> Name('Doe', 'John')
    Name(last='Doe', first='John', middle=None)
    >>> Name(first='Jane', last='Doe', middle='Kim')
    Name(last='Doe', first='Jane', middle='Kim')
    >>> Name('Smith', 'John', 'Robert')
    Name(last='Smith', first='John', middle='Robert')
    """
    result = collections.namedtuple(typename, args + tuple(kwargs))
    result.__new__.__defaults__ = tuple(kwargs.values())
    kwargs_list = repr(kwargs)[1:-1].replace(': ', '=')
    arg_list = repr(args)[1:-1]
    arg_list = (arg_list + ', ' + kwargs_list).replace("'", '')
    result.__doc__ = f'{typename}({arg_list})'
    return result
