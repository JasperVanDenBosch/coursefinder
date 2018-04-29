#!/usr/bin/python
# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages


setup(
    name='coursefinder',
    version='0.0',
    author='Jasper J.F. van den Bosch',
    author_email='japsai@gmail.com',
    description='recommends UK courses by industry',
    packages=find_packages(),
    url = 'https://github.com/ilogue/coursefinder',
    test_suite="tests",
    scripts=['exe/coursefinder'],
    zip_safe=False,
    classifiers=[
    "Programming Language :: Python",
    "Framework :: Pyramid",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    install_requires=[],
    include_package_data=True,
    entry_points="""\
    [paste.app_factory]
    main = coursefinder.web:main
    """,
)
