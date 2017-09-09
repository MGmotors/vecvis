"""
A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from os import path
from setuptools import setup, find_packages


HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    LONG_DESC = f.read()

setup(
    name = "vecvis",
    version = "0.2",
    description= "A module for showing and filtering vectors",
    long_description = LONG_DESC,
    url = "https://gitlab.fsi.hochschule-trier.de/goertzm/bachelor",
    author="Moritz Goertz",
    author_email="goertzm@hochschule-trier.de",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5"
        ],
    keywords="? a",
    packages=find_packages(exclude=["contrib", "docs", "tests", "run"]),
    )
