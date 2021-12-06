"""
Easy-to-import Python module with a basic, efficient, native implementation
of the extended Euclidean algorithm.
"""
from __future__ import annotations
from typing import Tuple
import doctest

def egcd(b: int, n: int) -> Tuple[int, int, int]:
    # pylint: disable=C0301
    """
    Given two integers ``(b, n)``, returns ``(gcd(b, n), a, m)`` such that
    ``a*b + n*m = gcd(b, n)``.

    This implementation is adapted from the sources below:
    * ``https://brilliant.org/wiki/extended-euclidean-algorithm/``
    * ``https://rosettacode.org/wiki/Modular_inverse``
    * ``https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm``
    * ``https://en.wikipedia.org/wiki/Euclidean_algorithm``

    >>> egcd(1, 1)
    (1, 0, 1)
    >>> egcd(12, 8)
    (4, 1, -1)
    >>> egcd(23894798501898, 23948178468116)
    (2, 2437250447493, -2431817869532)
    >>> egcd(pow(2, 50), pow(3, 50))
    (1, -260414429242905345185687, 408415383037561)
    >>> from math import gcd
    >>> checks = []
    >>> for (b, n) in [(b, n) for b in range(200) for n in range(200)]:
    ...    (g, a, m) = egcd(b, n)
    ...    checks.append(g == a*b + n*m)
    ...    checks.append(g == gcd(b, n))
    >>> all(checks)
    True
    """
    (x0, x1, y0, y1) = (1, 0, 0, 1)
    while n != 0:
        (q, b, n) = (b // n, n, b % n)
        (x0, x1) = (x1, x0 - q * x1)
        (y0, y1) = (y1, y0 - q * y1)
    return (b, x0, y0)

if __name__ == "__main__":
    doctest.testmod() # pragma: no cover
