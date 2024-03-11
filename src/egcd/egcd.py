"""
Pure-Python
`extended Euclidean algorithm <https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm>`__
implementation that accepts any number of integer arguments.
"""
from __future__ import annotations
from typing import Tuple
import doctest

def egcd(*integers: int) -> Tuple[int, ...]:
    # pylint: disable=line-too-long # Accommodate long link URLs on docstring.
    """
    To support the most typical use case, this function accepts two integers ``a``
    and ``b`` and returns a tuple of the form ``(g, s, t)`` such that ``g`` is the
    `greatest common divisor <https://en.wikipedia.org/wiki/Greatest_common_divisor>`__
    of ``a`` and ``b`` and such that the
    `identity <https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity>`__
    ``g == (a * s)  + (b * t)`` is satisfied.

    >>> egcd(1, 1)
    (1, 0, 1)
    >>> egcd(12, 8)
    (4, 1, -1)
    >>> 4 == (1 * 12) + ((-1) * 8)
    True
    >>> egcd(23894798501898, 23948178468116)
    (2, 2437250447493, -2431817869532)
    >>> egcd(pow(2, 50), pow(3, 50))
    (1, -260414429242905345185687, 408415383037561)

    This implementation has been adapted from the algorithms listed below
    (and subsequently expanded to support any number of integer inputs):

    * `Extended Euclidean Algorithm <https://brilliant.org/wiki/extended-euclidean-algorithm/>`__
      on `Brilliant.org <https://brilliant.org>`__,
    * `Modular inverse <https://rosettacode.org/wiki/Modular_inverse>`__
      on `Rosetta Code <https://rosettacode.org>`__,
    * `Algorithm Implementation/Mathematics/Extended Euclidean algorithm <https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm>`__
      on `Wikibooks <https://en.wikibooks.org>`__, and
    * `Extended Euclidean algorithm <https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm>`__
      on `Wikipedia <https://en.wikipedia.org>`__.

    This function can accept any number of integer arguments (as the built-in
    function :obj:`math.gcd` does in Python 3.9 and higher). In general,
    the greatest common divisor of *all* the arguments is returned (along
    with coefficients that satisfy the generalized form of the associated
    `identity <https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity>`__).

    >>> egcd(2, 2, 3)
    (1, 0, -1, 1)
    >>> egcd(13, 16, 17)
    (1, 5, -4, 0)
    >>> egcd(2, 4, 3, 9)
    (1, -1, 0, 1, 0)
    >>> 1 == ((-1) * 2) + (0 * 4) + (1 * 3) + (0 * 9)
    True

    This function conforms to the behavior of :obj:`math.gcd` when all arguments
    are ``0`` (returning ``0`` as the greatest common divisor) or when any of the
    arguments are negative (returning the largest *positive* integer that is a
    divisor of all the arguments).

    >>> egcd(0, 0)
    (0, 1, 0)
    >>> egcd(-25, -15)
    (5, 1, -2)
    >>> egcd(-9, 6, -33, -3)
    (3, 0, 0, 0, -1)

    To conform to the behavior of :obj:`math.gcd` in its base cases (in Python
    3.9 and higher), this function returns ``(0,)`` when there are no arguments
    and the sole argument paired with the coefficient ``1`` when only one
    argument is supplied.

    >>> egcd()
    (0,)
    >>> egcd(5)
    (5, 1)

    A succinct way to extract the greatest common divisor and the
    coefficients is to take advantage of Python's support for
    `iterable unpacking <https://peps.python.org/pep-3132/>`__ via the
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
    input pairs using the built-in :obj:`math.gcd` function.

    >>> from math import gcd
    >>> from itertools import product
    >>> checks = []
    >>> for (a, b) in product(range(-1000, 1000), range(-1000, 1000)):
    ...    (g, s, t) = egcd(a, b)
    ...    assert(g == gcd(a, b))
    ...    assert(g == (a * s) + (b * t))

    The more complex example below tests the behavior of this function over
    a range of input sequences. The function ``gcd_`` below is introduced to
    ensure that the example is compatible with Python 3.7 and 3.8.

    >>> from functools import reduce
    >>> gcd_ = lambda *bs: reduce(gcd, bs, bs[0]) # Backwards-compatible.
    >>> checks = []
    >>> for k in range(1, 5):
    ...    for bs in product(*([range(-50 // k, 50 // k)] * k)):
    ...        (g, *cs) = egcd(*bs)
    ...        assert(g == gcd_(*bs))
    ...        assert(g == sum(c * b for (c, b) in zip(cs, bs)))
    """
    if len(integers) == 0:
        return (0,)

    (g, cs) = (integers[0], [1]) # Running accumulators for the results.
    for (i, a) in enumerate(integers):
        if not isinstance(a, int): # Check type of all arguments.
            raise TypeError(
                "'" + type(a).__name__ + "'" +
                ' object cannot be interpreted as an integer'
            )
        if i == 0: # First argument is already assigned to ``g``.
            continue

        # Perform an iterative version of the extended Euclidean algorithm for
        # the pair of inputs ``g`` and ``a``.
        (s, t, x0, x1, y0, y1) = (g, a, 1, 0, 0, 1)
        while t != 0:
            (q, s, t) = (s // t, t, s % t)
            (x0, x1) = (x1, x0 - q * x1)
            (y0, y1) = (y1, y0 - q * y1)

        # Assign the result of the two-argument algorithm to the running
        # accumulators.
        (g, s, t) = (s, x0, y0)
        cs = [c * s for c in cs] + [t]

    # To conform to the behavior of ``math.gcd``, always return the greatest
    # common divisor as a nonnegative integer (adjusting the coefficients
    # accordingly, if necessary).
    return tuple([abs(g)] + ([-c for c in cs] if g < 0 else cs))

if __name__ == '__main__':
    doctest.testmod() # pragma: no cover
