skrt v1.2.0
=============

containers
----------
Specialized containers as alternatives to Python's built-in types and to those
defined in the collections standard module.

* **defaultnamedtuple**  factory function for namedtuples with default arguments
* **forwardingdict**     defaultdict subclass that passes missing key to factory

utils
-----
Utility functions for manipulating containers.
Thanks `Jack Fischer
<https://www.github.com/jackfischer/>`_, for the idea for ``rmap``.

* **subdict**  extract a subset of a dictionary
* **match**    compare multiple objects based on a list of shared attributes
* **rmap**     recursively map a function onto items of nested containers

text
----
Utilities for manipulating text.

* **color**    add ansi colors and styles to strings
