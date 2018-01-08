from setuptools import setup

setup(
    name             = 'egcd',
    version          = '0.0.1.0',
    packages         = ['egcd',],
    install_requires = [],
    license          = 'MIT',
    url              = 'https://github.com/lapets/egcd',
    author           = 'Andrei Lapets',
    author_email     = 'a@lapets.io',
    description      = 'Easy-to-import Python module with a basic, efficient, native implementation of the extended Euclidean algorithm.',
    long_description = open('README.rst').read(),
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
)
