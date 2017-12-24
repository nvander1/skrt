"""This module implements higher order functions found in languages
like Haskell.

* compose  compose a list of functions
* flip     create a function with reversed arguments of another function
* foldl    left-associative reduce
* foldr    right-associatve reduce
"""


from functools import reduce

from .utils import last, init


def foldl(function, acc, xs):
    """Reduces a sequence with a function in a left-associative manner.


    It is helpful to visualize the left-fold as the following transformation.

          foldl f acc [1, 2, 3, 4, 5]

        +                             f
       / \                           / \ 
    [1]   +                         f   5
         / \                       / \ 
      [2]   +                     f   4
           / \                   / \ 
        [3]   +                 f   3
             / \               / \ 
          [4]   +             f   2
               / \           / \ 
            [5]   []      acc   1

    Parameters
    ----------
    function : def function(x: B, y: A) -> B
        The combining function.
    acc : B
        The accumulating value.
    xs : Sequence[A]
        The sequence to fold.

    Returns
    -------
    B
        The reduced value.

    Examples
    --------
    >>> result = foldl(lambda x, y: x-y, 0, [1, 2, 3, 4, 5])
    >>> result == (((((0 - 1) - 2) - 3) - 4) - 5)
    True
    """
    return reduce(function, xs, acc)


def foldr(function, acc, xs):
    """Reduces a sequence with a function in a right-associative manner.


    It is helpful to visualize the right-fold as the following transformation.

         foldr f acc [1, 2, 3, 4, 5]

        +                           f
       / \                         / \ 
    [1]   +                       1   f
         / \                         / \ 
      [2]   +                       2   f
           / \                         / \ 
        [3]   +                       3   f
             / \                         / \ 
          [4]   +                       4   f
               / \                         / \ 
            [5]   []                      5   acc

    Parameters
    ----------
    function : def function(x: A, y: B) -> B
        The combining function.
    acc : B
        The accumulating value.
    xs : Sequence[A]
        The sequence to fold.

    Returns
    -------
    B
        The reduced value.

    Examples
    --------
    >>> result = foldr(lambda x, y: x-y, 0, [1, 2, 3, 4, 5])
    >>> result == (1 - (2 - (3 - (4 - (5 - 0)))))
    True
    """
    return reduce(lambda x, y: function(y, x), reversed(xs), acc)


def compose(*functions):
    """Composes a list of function.
    
    Parameters
    ----------
    functions : list
        A list of callables. The argument of the nth function should be of
        the same type as the return type of the n+1th function.

    Returns
    -------
    function
        A new function created by composing all the functions.

    Examples
    --------
    >>> double = lambda x: x*2
    >>> square = lambda x: x**2
    >>> compose(square, double)(3)
    36
    >>> (3 * 2) ** 2
    36
    """
    def composed(*args, **kwargs):
        acc = last(functions)(*args, **kwargs)
        return foldr(lambda f, v: f(v), acc, init(functions))
    return composed


def flip(func):
    """Reverses the arguments of a function.

    Parameters
    ----------
    func : function
        The original function.

    Returns
    -------
    function
        A function identical to `func` except it expects arguments in reverse.
    """
    def flipped(*args):
        return func(*args[::-1])
    return flipped
