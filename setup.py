"""Setup for to_words package."""
from setuptools import setup, find_packages

from wordsapp import AUTHOR, VERSION

name = 'words_app'

version = VERSION

setup(
    name=name,
    version=version,
    packages=find_packages(exclude=['tests', 'tests.*']),
    description="Numbers to words library",
    author=AUTHOR,
    author_email="dee.caranja@gmail.com",
    license="MIT",
    install_requires=[
    ],
    scripts=[
    ],
    include_package_data=True
)
