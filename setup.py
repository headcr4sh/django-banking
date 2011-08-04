#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
from distutils.core import setup

setup(
    name='django-banking',
    version='0.1-dev',
    description='Banking (SWIFT) classes for Python/Django',
    long_description=open('README').read(),
    author='Benjamin P. Jung',
    author_email='headcr4sh@gmail.com',
    url='https://github.com/headcr4sh/dango-banking',
    download_url='https://github.com/headcr4sh/django-banking/downloads/',
    packages = ['django_banking', 'django_banking.swift'],
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
