"""Implements utility functions for manipulating
containers.

* subdict  extract a subset of a dictionary
* match    compare multiple objects based on a list of shared attributes
* rmap     recursively map a function onto items of nested iterables

"""


def subdict(keys, dict_):
    """
    Creates a subdictionary given a list of keys and a dictionary.

    Parameters
    ----------
    keys : list
        Keys to extract from `dict_`.
    dict_ : dict
        The dictionary from which to extract values.

    Returns
    -------
    dict
        A dictionary whose elements are a subset of `dict_`'s.

    Raises
    ------
    KeyError
        If any item in `keys` is not present in `dict_`.

    Examples
    --------
    >>> a = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
    >>> subdict(['two', 'four'], a)
    {'two': 2, 'four': 4}
    >>> subdict(['five'], a)
    Traceback (most recent call last):
        ...
    KeyError: 'five'

    """
    return {key: dict_[key] for key in keys}


def match(fields, objs):
    """
    Compares a list of objects based on a list of common attributes.

    Parameters
    ----------
    fields : list of str
        Attributes common to each object in `objs`.
    objs : list of objects
        Objects that are instances of defined classes.
        Only class instances have __dict__ attribute.
        Instances of types defined by namedtuples will not work.

    Returns
    -------
    bool
        True if attributes match in all objects.

    Raises
    ------
    KeyError
        if any field in `fields` is not present in an object in `objs`.

    Examples
    --------
    >>> A = type('A', (), dict(a=1, b=2, c=3, d=4))
    >>> B = type('B', (), dict(c=3, d=4, e=5))
    >>> match(['c', 'd'], [A, B])
    True

    """
    subdicts = [subdict(fields, d) for d in [obj.__dict__ for obj in objs]]
    return all(dict_ == subdicts[0] for dict_ in subdicts)


def rmap(obj, func, typename):
    """
    Recursivley maps a function onto an object or elements of a container.

    Parameters
    ----------
    obj : object
        The object or container onto which `func` is recursively mapped.
    func : function
        The function to apply to the most deeply nested elements in obj.
    typename : type
        The type of argument taken by `func`.

    Examples
    --------
    >>> obj = [1, 2, 3, 4, '1']
    >>> rmap(obj, lambda x: x**2, int)
    [1, 4, 9, 16, '1']

    >>> obj = [1, 2, 3, 4, 'Word', {'WORD': 'WORD'}]
    >>> rmap(obj, lambda x: x.lower(), str)
    [1, 2, 3, 4, 'word', {'WORD': 'word'}]

    """
    if isinstance(obj, typename):
        return func(obj)
    if hasattr(obj, '__iter__'):
        gen = (rmap(item, func, typename) for item in obj)
    return (list(gen)  if isinstance(obj, list) else
            tuple(gen) if isinstance(obj, tuple) else
            set(gen)   if isinstance(obj, set) else
            {k: rmap(v, func, typename)
             for k, v in obj.items()} if isinstance(obj, dict) else
            obj)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
