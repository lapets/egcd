====
egcd
====

Easy-to-import library with a basic, efficient, pure-Python implementation of the extended Euclidean algorithm.

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
.. _egcd: https://egcd.readthedocs.io/en/0.5.0/_source/egcd.html#egcd.egcd.egcd

The function |egcd|_ is an efficient implementation of the `extended Euclidean algorithm <https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm>`__. It accepts two integer inputs ``b`` and ``n``, returning a tuple of the form ``(gcd(b, n), a, m)`` where the three integers in the tuple satisfy the `identity <https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity>`__ ``(a * b) + (n * m) == gcd(b, n)``:

.. code-block:: python

    >>> egcd(1, 1)
    (1, 0, 1)
    >>> egcd(12, 8)
    (4, 1, -1)
    >>> egcd(23894798501898, 23948178468116)
    (2, 2437250447493, -2431817869532)
    >>> egcd(pow(2, 50), pow(3, 50))
    (1, -260414429242905345185687, 408415383037561)

Development
-----------
All installation and development dependencies are fully specified in ``pyproject.toml``. The ``project.optional-dependencies`` object is used to `specify optional requirements <https://peps.python.org/pep-0621>`__ for various development tasks. This makes it possible to specify additional options (such as ``docs``, ``lint``, and so on) when performing installation using `pip <https://pypi.org/project/pip>`__:

.. code-block:: bash

    python -m pip install .[docs,lint]

Documentation
^^^^^^^^^^^^^
The documentation can be generated automatically from the source files using `Sphinx <https://www.sphinx-doc.org>`__:

.. code-block:: bash

    python -m pip install .[docs]
    cd docs
    sphinx-apidoc -f -E --templatedir=_templates -o _source .. && make html

Testing and Conventions
^^^^^^^^^^^^^^^^^^^^^^^
All unit tests are executed and their coverage is measured when using `pytest <https://docs.pytest.org>`__ (see the ``pyproject.toml`` file for configuration details):

.. code-block:: bash

    python -m pip install .[test]
    python -m pytest

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`__:

.. code-block:: bash

    python src/egcd/egcd.py -v

Style conventions are enforced using `Pylint <https://pylint.readthedocs.io>`__:

.. code-block:: bash

    python -m pip install .[lint]
    python -m pylint src/egcd

Contributions
^^^^^^^^^^^^^
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/lapets/egcd>`__ for this library.

Versioning
^^^^^^^^^^
Beginning with version 0.1.0, the version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`__.

Publishing
^^^^^^^^^^
This library can be published as a `package on PyPI <https://pypi.org/project/egcd>`__ by a package maintainer. First, install the dependencies required for packaging and publishing:

.. code-block:: bash

    python -m pip install .[publish]

Ensure that the correct version number appears in ``pyproject.toml``, and that any links in this README document to the Read the Docs documentation of this package (or its dependencies) have appropriate version numbers. Also ensure that the Read the Docs project for this library has an `automation rule <https://docs.readthedocs.io/en/stable/automation-rules.html>`__ that activates and sets as the default all tagged versions. Create and push a tag for this version (replacing ``?.?.?`` with the version number):

.. code-block:: bash

    git tag ?.?.?
    git push origin ?.?.?

Remove any old build/distribution files. Then, package the source into a distribution archive:

.. code-block:: bash

    rm -rf build dist src/*.egg-info
    python -m build --sdist --wheel .

Finally, upload the package distribution archive to `PyPI <https://pypi.org>`__:

.. code-block:: bash

    python -m twine upload dist/*
