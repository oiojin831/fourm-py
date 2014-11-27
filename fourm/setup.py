# --*-- encoding: utf-8 -*-
""":mod:`setup` --- Setup
~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import setuptools
from setuptools import setup

requires = [
    'Flask',
    'SQLAlchemy',
    'Flask-SQLAlchemy',
    'pyScss',
]

setup(
    name='fourm',
    version='0.1.0',
    author='EungJin Lee',
    description='Simple website for restaurants using instagram',
    long_description=__doc__,
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=requires,
    classifiers=[
        'Environment :: Wev Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    ],
)