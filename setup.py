import os
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md") as f:
    readme = f.read()

classifiers = [
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    ]

setup(
    name = "babypandas",
    version = "0.0.1",
    description = "A small pure python library with Pandas like API",
    long_description = readme,
    packages = ['babypandas', 'babypandas.tests'],
    package_dir = { 'babypandas' : 'src', 'babypandas.tests' : 'tests' },
    install_requires = [ ],
    author = "aegorenkov",
    maintainer = "Dilawar Singh",
    maintainer_email = "dilawars@ncbs.res.in",
    url = "http://github.com/dilawar/",
    license='GPL?',
    classifiers=classifiers,
)
