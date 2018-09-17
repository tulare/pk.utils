# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages

# Get version without import module
exec(compile(open('pk/utils/version.py').read(),
             'pk/utils/version.py', 'exec'))

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-dependencies
]

with open('README.md') as f :
    readme = f.read()

with open('LICENSE') as f :
    license = f.read()

setup(
    name='pk.utils',
    version=__version__,
    description='Various utilities for python',
    long_description=readme,
    author='Tulare Regnus',
    author_email='tulare.paxgalactica@gmail.com',
    url='https://github.com/tulare/pk.utils',
    license=license,
    packages=find_packages(exclude=('tests',)),
    namespace_packages=['pk'],
    zip_safe=False,
    install_requires=install_requires
)
