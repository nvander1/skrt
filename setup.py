"""Setup module for nik.

See:
https://github.com/nvander1/nik
"""

from codecs import open
from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nik',
    version='1.0.0',
    description='Nifty tools and containers',
    long_description=long_description,
    url='https://github.com/nvander1/nik',
    author='Nik Vanderhoof',
    author_email='pypi@vanderhoof.pw',
    license='GPLv3',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='development tools containers',
    packages=['nik'],
    python_requires='~=3.6'
)
