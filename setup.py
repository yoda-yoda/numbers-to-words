"""Setup for to_words package."""
from setuptools import setup, find_packages

from wordsapp import AUTHOR, VERSION

name = 'words_app'


def get_version(version_iter):
    """Get the version number."""
    assert isinstance(version_iter, (tuple, list,)) is True
    version = ''
    for number in version_iter:
        version += str(number) + '.'
    return version[:len(version) - 1]

version = get_version(VERSION)

setup(
    name=name,
    version=version,
    packages=find_packages(exclude=['tests', 'tests.*']),
    description='Numbers to words library',
    author=AUTHOR,
    author_email='dee.caranja@gmail.com',
    license='MIT',
    install_requires=[
    ],
    scripts=[
    ],
    include_package_data=True
)
