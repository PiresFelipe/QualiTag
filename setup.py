# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as file:
    readme = file.read()

with open("LICENSE", encoding="utf-8") as file:
    _license = file.read()

setup(
    name="QualiTag",
    version="0.1.0",
    description="",
    long_description=readme,
    author="Felipe Pires dos Santos",
    author_email="felipepires725@gmail.com",
    url="",
    license=_license,
    packages=find_packages(exclude=("tests", "docs")),
)
