#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dewildcard",
    # packages = ['dewildcard'],
    scripts=['dewildcard'],
    version="0.2.1",
    description="Expand wildcard imports in Python code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Quentin Stafford-Fraser",
    author_email="quentin@pobox.com",
    url="http://github.com/quentinsf/dewildcard",
    download_url='https://github.com/quentinsf/dewildcard/tarball/0.2',
    keywords='pylint',
    classifiers=(
        "Programming Language :: Python :: 2",
    )
)

