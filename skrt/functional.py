"""This module implements higher order functions found in languages
like Haskell.

* foldl  left-associative reduce
* foldr  right-associatve reduce
"""


from functools import reduce


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
