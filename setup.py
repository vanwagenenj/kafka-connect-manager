#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['click==7.0', 'bumpversion==0.5.3']

setup_requirements = ['pytest-runner', ]

test_requirements = ['flake8==3.6.0',
                     'pytest==4.0.2',
                     'pytest-flake8==1.0.2']

setup(

    name='cp-kafka-connect-manager',
    description="Python client for managing Confluent Kafka connectors",
    author="Angelo Fausti",
    author_email='afausti@lsst.org',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=['connect_manager'],
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords=['kafka',
              'confluent',
              'connector'
              'influxdb'],
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/lsst-sqre/cp-kafka-connect-manager',
    version='0.1.0',
    entry_points={
        'console_scripts': ['connect_manager = connect_manager.main:main']
    }
)