#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "temp-o-mat",
    version = "0.1",
    packages = find_packages(),
    scripts = ['src/daemon.py'],
    
    install_requires = open("requirements.txt").read().split("\n"),

    # metadata for upload to PyPI
    author = "Philipp Engel",
    author_email = "mail@philippengel.de",
    description = "Daemon for collecting and publishing temperature sensor data",
)
