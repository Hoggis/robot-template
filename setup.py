"""
Robot Project setup.
"""
import sys
from setuptools import setup, find_packages

if not sys.version_info[0] == 3:
    sys.exit("Only Python 3 is supported")

readme = open('README.rst').read()


def get_install_requires():
    """
    Read requirements.txt into a list. Use this only if
    you want to create an installable package.

    Note that this doesn't work if using a custom pip index
    or a package from git. Installable package should
    anyway use only PyPi published packages as their requirements.
    """
    return open("requirements.txt").read()


def get_tests_require():
    """
    Read requirements-dev.txt into a list.

    This contains dependencies required to run tests and linters.

    Note that this doesn't work if using a custom pip index
    or a package from git. Installable package should
    anyway use only PyPi published packages as their requirements.
    """
    return open("requirements-test.txt").read() + open("requirements-dev.txt").read()


# Additional Pytest requirements
setup_requires = [
    "pytest-runner",
]

setup(
    name="Project-name-here",
    packages=find_packages(),
    version="1",
    url="",
    license="",
    author="Siili Solutions Oyj, Intelligent Automation",
    author_email="ia@siili.com",
    description=__doc__,
    long_description=readme,
    install_requires=get_install_requires(),
    setup_requires=setup_requires,
    tests_require=get_tests_require(),
)
