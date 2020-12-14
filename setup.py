#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Node2Vec installation
import codecs
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

with open(os.path.join(here, "node2vec", "version.py")) as fp:
    exec(fp.read())

setup(
    name="node2vec",
    version=__version__,  # noqa: F821
    author="Aditya Grover",
    author_email="adityag@cs.stanford.edu",
    packages=find_packages(),
    package_data={"": ["LICENSE"],},
    url="https://github.com/ch3njust1n/node2vec",
    license="MIT",
    entry_points={"console_scripts": ["node2vec = node2vec.cli:main",],},
    install_requires=["networkx", "numpy", "gensim"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Terminals",
        "Topic :: Utilities",
    ],
    description=("node2vec algorithm learns continuous representations for nodes in any (un)directed, (un)weighted graph"),
    include_package_data=True,
    long_description_content_type="text/markdown",
    long_description=long_description,
    zip_safe=True,
    python_requires=">=3.6",
    project_urls={
        "Bug Reports": "https://github.com/aditya-grover/node2vec/issues"
    },
    keywords=["python3", "node2vec", "machine learning", "graphs", "graph representation learning",],
)