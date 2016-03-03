#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

path_readme = os.path.join(os.path.dirname(__file__), 'README.md')
try:
    import pypandoc
    README = pypandoc.convert(path_readme, 'rst')
except (IOError, ImportError):
    with open(path_readme) as readme:
        README = readme.read()

setup(
    name='nilandapi',
    version='1.0.0',
    license='MIT License',
    packages=['nilandapi'],
    install_requires=['requests[security] >= 2.9.1'],
    description='Niland API Client for Python',
    long_description=README,
    author='Niland Team',
    author_email='support@niland.io',
    url='https://github.com/niland/api-client-python',
    keywords=['niland', 'pyniland', 'music', 'search', 'recommendation', 'hosted', 'cloud', 'tagging'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Development Status :: 5 - Production/Stable',
    ]
)
