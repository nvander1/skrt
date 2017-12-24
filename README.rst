skrt v1.2.1
=============

containers
----------
Specialized containers as alternatives to Python's built-in types and to those
defined in the collections standard module.

* **defaultnamedtuple**  factory function for namedtuples with default arguments
* **forwardingdict**     defaultdict subclass that passes missing key to factory


functional
----------
Higher order functions like those found in languages like Haskell.

* **foldl**  left-associative reduce
* **foldr**  right-associatve reduce


text
----
Utilities for manipulating text.

* **color**    add ansi colors and styles to strings


utils
-----
Utility functions for manipulating containers.
Thanks `Jack Fischer
<https://www.github.com/jackfischer/>`_, for the idea for ``rmap``.

* **subdict**  extract a subset of a dictionary
* **match**    compare multiple objects based on a list of shared attributes
* **rmap**     recursively map a function onto items of nested containers

* **head**     get the first element of a sequence
* **tail**     get all but the first element of a sequence
* **last**     get the last element of a sequence
* **init**     get all but the last element of a sequence
