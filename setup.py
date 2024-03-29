#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import io
from setuptools import setup, find_packages

with io.open('README.rst', encoding='utf-8') as readme_file, io.open(
    'HISTORY.rst', encoding='utf-8'
) as history_file:
    long_description = (readme_file.read() + "\n\n" + history_file.read())

install_requires = [
    'click>=6.0',
    # TODO: put package requirements here
]

setup_requires = [
    'pytest-runner',
    # TODO(starofrainnight): put setup requirements (distutils extensions, etc.) here
]

tests_requires = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='google-style-pre-commit-hooks',
    version="0.0.1",
    description="A series pre-commit hooks that support format source by google style",
    long_description=long_description,
    author="Hong-She Liang",
    author_email='starofrainnight@gmail.com',
    url='https://github.com/starofrainnight/google-style-pre-commit-hooks',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'google-style-pre-commit-hooks=googlestyleprecommithooks.__main__:main'
        ]
    },
    include_package_data=True,
    install_requires=install_requires,
    license="Apache Software License",
    zip_safe=False,
    keywords='googlestyleprecommithooks,google-style-pre-commit-hooks',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=tests_requires,
    setup_requires=setup_requires,
)
