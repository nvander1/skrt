"""Setup module for skrt.

See:
https://github.com/nvander1/skrt
"""

from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='skrt',
    version='1.0.0.0',
    description='Nifty tools and containers',
    long_description=readme,
    url='https://github.com/nvander1/skrt',
    author='Nik Vanderhoof',
    author_email='pypi@vanderhoof.pw',
    license='AGPLv3',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='development tools containers',
    packages=['skrt'],
    python_requires='~=3.6'
)
