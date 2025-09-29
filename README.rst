====
egcd
====

Pure-Python `extended Euclidean algorithm <https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm>`__ implementation that accepts any number of integer arguments.

|pypi| |readthedocs| |actions| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/egcd.svg#
   :target: https://badge.fury.io/py/egcd
   :alt: PyPI version and link.

.. |readthedocs| image:: https://readthedocs.org/projects/egcd/badge/?version=latest
   :target: https://egcd.readthedocs.io/en/latest/?badge=latest
   :alt: Read the Docs documentation status.

.. |actions| image:: https://github.com/lapets/egcd/workflows/lint-test-cover-docs/badge.svg#
   :target: https://github.com/lapets/egcd/actions/workflows/lint-test-cover-docs.yml
   :alt: GitHub Actions status.

.. |coveralls| image:: https://coveralls.io/repos/github/lapets/egcd/badge.svg?branch=main
   :target: https://coveralls.io/github/lapets/egcd?branch=main
   :alt: Coveralls test coverage summary.

Installation and Usage
----------------------
This library is available as a `package on PyPI <https://pypi.org/project/egcd>`__:

.. code-block:: bash

    python -m pip install egcd

The library can be imported in the usual way:

.. code-block:: python

    from egcd import egcd

Examples
^^^^^^^^

.. |egcd| replace:: ``egcd``
.. _egcd: https://egcd.readthedocs.io/en/3.0.0/_source/egcd.html#egcd.egcd.egcd

.. |math_gcd| replace:: ``math.gcd``
.. _math_gcd: https://docs.python.org/3/library/math.html#math.gcd

The function |egcd|_ is a pure-Python implementation of the `extended Euclidean algorithm <https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm>`__ that can be viewed as an expansion of the functionality and interface of the built-in |math_gcd|_ function. When it is supplied two integer arguments ``a`` and ``b``, it returns a tuple of the form ``(g, s, t)`` where the three integers in the tuple satisfy the `identity <https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity>`__ ``(a * s) + (b * t) == g``:

.. code-block:: python

    >>> egcd(1, 1)
    (1, 0, 1)
    >>> egcd(12, 8)
    (4, 1, -1)
    >>> egcd(23894798501898, 23948178468116)
    (2, 2437250447493, -2431817869532)
    >>> egcd(pow(2, 50), pow(3, 50))
    (1, -260414429242905345185687, 408415383037561)

However, any number of integer arguments can be supplied. When no arguments are supplied, the result is ``(0,)`` (just as the expression ``math.gcd()`` evaluates to ``0`` in Python 3.9 and higher). In all other cases, the result contains the `greatest common divisor <https://en.wikipedia.org/wiki/Greatest_common_divisor>`__ of all the supplied integers and the coefficients of the generalized form of the associated `identity <https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity>`__:

.. code-block:: python

    >>> egcd(2, 4, 3, 9)
    (1, -1, 0, 1, 0)
    >>> 1 == ((-1) * 2) + (0 * 4) + (1 * 3) + (0 * 9)
    1

A succinct way to extract the greatest common divisor and the coefficients is to take advantage of Python's support for `iterable unpacking <https://peps.python.org/pep-3132/>`__ via the `asterisk <https://docs.python.org/3/reference/expressions.html#expression-lists>`__ notation:

.. code-block:: python

    >>> bs = (26, 16, 34)
    >>> (g, *cs) = egcd(*bs)
    >>> (g, cs)
    (2, [-3, 5, 0])
    >>> g == sum(c * b for (c, b) in zip(cs, bs))
    True

Development
-----------
All installation and development dependencies are fully specified in ``pyproject.toml``. The ``project.optional-dependencies`` object is used to `specify optional requirements <https://peps.python.org/pep-0621>`__ for various development tasks. This makes it possible to specify additional options (such as ``docs``, ``lint``, and so on) when performing installation using `pip <https://pypi.org/project/pip>`__:

.. code-block:: bash

    python -m pip install ".[docs,lint]"

Documentation
^^^^^^^^^^^^^
The documentation can be generated automatically from the source files using `Sphinx <https://www.sphinx-doc.org>`__:

.. code-block:: bash

    python -m pip install ".[docs]"
    cd docs
    sphinx-apidoc -f -E --templatedir=_templates -o _source .. && make html

Testing and Conventions
^^^^^^^^^^^^^^^^^^^^^^^
All unit tests are executed and their coverage is measured when using `pytest <https://docs.pytest.org>`__ (see the ``pyproject.toml`` file for configuration details):

.. code-block:: bash

    python -m pip install ".[test]"
    python -m pytest

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`__:

.. code-block:: bash

    python src/egcd/egcd.py -v

Style conventions are enforced using `Pylint <https://pylint.readthedocs.io>`__:

.. code-block:: bash

    python -m pip install ".[lint]"
    python -m pylint src/egcd

Contributions
^^^^^^^^^^^^^
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/lapets/egcd>`__ for this library.

Versioning
^^^^^^^^^^
Beginning with version 0.1.0, the version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`__.

Publishing
^^^^^^^^^^
This library can be published as a `package on PyPI <https://pypi.org/project/egcd>`__ via the GitHub Actions workflow found in ``.github/workflows/build-publish-sign-release.yml`` that follows the `recommendations found in the Python Packaging User Guide <https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/>`__.

Ensure that the correct version number appears in ``pyproject.toml``, and that any links in this README document to the Read the Docs documentation of this package (or its dependencies) have appropriate version numbers. Also ensure that the Read the Docs project for this library has an `automation rule <https://docs.readthedocs.io/en/stable/automation-rules.html>`__ that activates and sets as the default all tagged versions.

To publish the package, create and push a tag for the version being published (replacing ``?.?.?`` with the version number):

.. code-block:: bash

    git tag ?.?.?
    git push origin ?.?.?
