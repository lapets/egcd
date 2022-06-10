====
egcd
====

Easy-to-import Python module with a basic, efficient, native implementation of the extended Euclidean algorithm.

|pypi| |readthedocs| |actions| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/egcd.svg
   :target: https://badge.fury.io/py/egcd
   :alt: PyPI version and link.

.. |readthedocs| image:: https://readthedocs.org/projects/egcd/badge/?version=latest
   :target: https://egcd.readthedocs.io/en/latest/?badge=latest
   :alt: Read the Docs documentation status.

.. |actions| image:: https://github.com/lapets/egcd/workflows/lint-test-cover-docs/badge.svg
   :target: https://github.com/lapets/egcd/actions/workflows/lint-test-cover-docs.yml
   :alt: GitHub Actions status.

.. |coveralls| image:: https://coveralls.io/repos/github/lapets/egcd/badge.svg?branch=main
   :target: https://coveralls.io/github/lapets/egcd?branch=main
   :alt: Coveralls test coverage summary.

Package Installation and Usage
------------------------------
The package is available on `PyPI <https://pypi.org/project/egcd>`__::

    python -m pip install egcd

The library can be imported in the usual way::

    from egcd import egcd

The function ``egcd`` is an efficient implementation of the `extended Euclidean algorithm <https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm>`__. It accepts two integer inputs ``b`` and ``n``, returning a tuple of the form ``(gcd(b, n), a, m)`` where the three integers in the tuple satisfy the `identity <https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity>`__ ``(a * b) + (n * m) == gcd(b, n)``::

    >>> egcd(1, 1)
    (1, 0, 1)
    >>> egcd(12, 8)
    (4, 1, -1)
    >>> egcd(23894798501898, 23948178468116)
    (2, 2437250447493, -2431817869532)
    >>> egcd(pow(2, 50), pow(3, 50))
    (1, -260414429242905345185687, 408415383037561)

Documentation
-------------
.. include:: toc.rst

The documentation can be generated automatically from the source files using `Sphinx <https://www.sphinx-doc.org/>`__::

    cd docs
    python -m pip install -r requirements.txt
    sphinx-apidoc -f -E --templatedir=_templates -o _source .. ../setup.py && make html

Testing and Conventions
-----------------------
All unit tests are executed and their coverage is measured when using `pytest <https://docs.pytest.org>`__ (see ``setup.cfg`` for configuration details)::

    python -m pip install pytest pytest-cov
    python -m pytest

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`__::

    python egcd/egcd.py -v

Style conventions are enforced using `Pylint <https://www.pylint.org>`__::

    python -m pip install pylint
    python -m pylint egcd

Contributions
-------------
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/lapets/egcd>`__ for this library.

Versioning
----------
Beginning with version 0.1.0, the version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`__.

Publishing
----------
This library can be published as a `package on PyPI <https://pypi.org/project/egcd>`__ by a package maintainer. Install the `wheel <https://pypi.org/project/wheel>`__ package, remove any old build/distribution files, and package the source into a distribution archive::

    python -m pip install wheel
    rm -rf dist *.egg-info
    python setup.py sdist bdist_wheel

Next, install the `twine <https://pypi.org/project/twine>`__ package and upload the package distribution archive to `PyPI <https://pypi.org>`__::

    python -m pip install twine
    python -m twine upload dist/*
