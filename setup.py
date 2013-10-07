#!/usr/bin/env python

__author__ = 'Jason Corbett'

import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name="slickqa-snot",
    description="A plugin to nose to allow results from python tests to be put into slick.",
    version="1.0" + open("build.txt").read(),
    license="License :: OSI Approved :: Apache Software License",
    long_description=open('README.txt').read(),
    packages=find_packages(exclude=['distribute_setup']),
    #package_data={'': ['*.txt', '*.rst', '*.html']},
    #include_package_data=True,
    install_requires=['slickqa>=2.0.34', 'nose'],
    author="Slick Developers",
    url="http://github.com/slickqa/snot",
    entry_points={
        'nose.plugins.0.10': [
            'snot = snot:SlickAsSnotPlugin'
        ]
    }
)