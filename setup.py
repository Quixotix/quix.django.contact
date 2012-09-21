import distribute_setup
distribute_setup.use_setuptools()

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

from quix.django.contact import get_version

setup(
    name = "quix.django.contact", 
    version = get_version(),
    description = "A simple contact form for Django websites.",
    long_description = read("README.rst"),
    author = "Micah Carrick",
    author_email = "micah@quixotix.com",
    url = "https://github.com/Quixotix/quix.django.contact",
    packages = find_packages(),
    namespace_packages = ["quix", "quix.django"],
    py_modules = ['distribute_setup',],
    license = "New BSD License",
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
    ],
)
