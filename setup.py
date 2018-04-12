"""Setup module for skrt.

See:
https://github.com/nvander1/skrt
"""

from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='skrt',
    version='1.3.2',
    description='Nifty tools and containers',
    long_description=readme,
    url='https://github.com/nvander1/skrt',
    author='Nik Vanderhoof',
    author_email='pypi@vanderhoof.pw',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='development tools containers',
    packages=['skrt'],
    python_requires='>=2.7'
)
