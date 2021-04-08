#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup

version = "1.0.0"

if sys.argv[-1] == 'publish':
    os.system('make release')
    sys.exit()

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    readme = f.read()

description = "Phone book using Django REST Framework."

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

server_packages = ['src', 'src.PhoneBook', 'src.contactsapp']
server_package_data = {'': ['*.py', '*.sqlite3', 'README.md']}

setup(
    name='PhoneBook',
    version=version,
    description=description,
    long_description=readme,
    author='Sushma Goutam',
    author_email='sushma.goutam@gmail.com',
    url='https://github.com/sushma-goutam/PhoneBook',
    packages=server_packages,
    #package_dir={'PhoneBook': 'src'},
    package_data=server_package_data,
    include_package_data=True,
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    install_requires=[
        'Django>=2.2,<3.2;python_version>="3.7"',
    ],
    license="BSD",
    zip_safe=False,
    py_modules=['src/__main__'],
    keywords='PhoneBook',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
    ],
)