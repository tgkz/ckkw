#!/usr/bin/env python3
from setuptools import setup, find_packages

setup (
    name='ckkw',
    version = '0.0.1',
    description = 'ckkw early version',
    packages = find_packages(),
    scripts = [ 'scripts/ckkkw.sh' ],
    entry_points={
        'console_scripts': [
            'ckkw = ckkw.ckkw:main',
            'addkkw = ckkw.addkkw:main',
        ],
    },
)
