"""
Pure-Python
`extended Euclidean algorithm <https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm>`__
implementation that supports any number of integer arguments.
"""
from __future__ import annotations
from typing import Tuple
import doctest

def egcd(*integers: int) -> Tuple[int, ...]:
    # pylint: disable=line-too-long # Accommodate long link URLs on docstring.
    """
    Given two integers ``a`` and ``b``, this function returns a tuple of the
    form ``(g, s, t)`` such that ``g`` is the greatest common divisor of ``a``
    and ``b`` and such that the identity ``g == (a * s)  + (b * t)`` is
    satisfied.

    This implementation is adapted from the sources below, and extended to
    support two or more integers:

    * `Extended Euclidean Algorithm <https://brilliant.org/wiki/extended-euclidean-algorithm/>`__
      on `Brilliant.org <https://brilliant.org>`__,
    * `Modular inverse <https://rosettacode.org/wiki/Modular_inverse>`__
      on `Rosetta Code <https://rosettacode.org>`__,
    * `Algorithm Implementation/Mathematics/Extended Euclidean algorithm <https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm>`__
      on `Wikibooks <https://en.wikibooks.org>`__, and
    * `Euclidean algorithm <https://en.wikipedia.org/wiki/Euclidean_algorithm>`__
      on `Wikipedia <https://en.wikipedia.org>`__.

    >>> egcd(1, 1)
    (1, 0, 1)
    >>> egcd(12, 8)
    (4, 1, -1)
    >>> egcd(23894798501898, 23948178468116)
    (2, 2437250447493, -2431817869532)
    >>> egcd(pow(2, 50), pow(3, 50))
    (1, -260414429242905345185687, 408415383037561)

    To support more than two inputs (as the built-in :obj:`math.gcd` does),
    this function can accept any number of inputs. In such cases, the greatest
    common divisor of all of the inputs is returned, along with coefficients
    that satisfy the generalized form of the identity.

    >>> egcd(2, 2, 3)
    (1, 0, -1, 1)
    >>> egcd(13, 16, 17)
    (1, 5, -4, 0)
    >>> egcd(2, 4, 3, 9)
    (1, -1, 0, 1, 0)

    To follow the behavior of :obj:`math.gcd` in its base cases, this function
    returns ``0`` if the input is empty and the sole entry if no arguments are
    is supplied.

    >>> egcd(5)
    (5, 1)
    >>> egcd()
    (0,)

    A succinct way to extract the greatest common divisor and the coefficients
    is to take advantage of Python's support for iterable unpacking via the
    `asterisk <https://docs.python.org/3/reference/expressions.html#expression-lists>`__
    notation.

    >>> bs = (26, 16, 34)
    >>> (g, *cs) = egcd(*bs)
    >>> (g, cs)
    (2, [-3, 5, 0])
    >>> g == sum(c * b for (c, b) in zip(cs, bs))
    True

    If an argument is not an integer, an exception is raised.

    >>> egcd(1.2, 3, 4)
    Traceback (most recent call last):
      ...
    TypeError: 'float' object cannot be interpreted as an integer

    >>> egcd(1, 2.3)
    Traceback (most recent call last):
      ...
    TypeError: 'float' object cannot be interpreted as an integer

    The example below tests the behavior of this function over a range of
    inputs using the built-in :obj:`math.gcd` function.


    The example below tests the behavior of this function over a range of
    input pairs using the built-in :obj:`math.gcd` function.

    >>> from math import gcd
    >>> from itertools import product
    >>> checks = []
    >>> for (a, b) in product(*([range(200)] * 2)):
    ...    (g, s, t) = egcd(a, b)
    ...    assert(g == gcd(a, b))
    ...    assert(g == (a * s) + (b * t))

    The more complex example below tests the behavior of this function over
    a range of input sequences.

    >>> checks = []
    >>> for k in range(1, 5):
    ...    for bs in product(*([range(100 // k)] * k)):
    ...        (g, *cs) = egcd(*bs)
    ...        assert(g == gcd(*bs))
    ...        assert(g == sum(c * b for (c, b) in zip(cs, bs)))
    """
    if len(integers) == 0:
        return (0,)

    (g, cs) = (integers[0], (1,))
    for (i, a) in enumerate(integers):
        if not isinstance(a, int): # Check type of all arguments.
            raise TypeError(
                "'" + type(a).__name__ + "'" +
                ' object cannot be interpreted as an integer'
            )
        if i == 0: # First argument is already assigned to ``g``.
            continue

        (s, t, x0, x1, y0, y1) = (g, a, 1, 0, 0, 1)
        while t != 0:
            (q, s, t) = (s // t, t, s % t)
            (x0, x1) = (x1, x0 - q * x1)
            (y0, y1) = (y1, y0 - q * y1)
        (g, s, t) = (s, x0, y0)
        cs = tuple(c * s for c in cs) + (t,)

    return (g,) + cs

if __name__ == '__main__':
    doctest.testmod() # pragma: no cover
