"""setup file for the package manager"""

from os.path import dirname, join
from setuptools import setup

with open(join(dirname(__file__), 'VERSION'), mode='r') as version_file:
    VERSION = version_file.read()

with open(join(dirname(__file__), 'README')) as readme_file:
    README = readme_file.read()

setup(
    name='STLInspector',
    version=VERSION,
    description='Systematic validation of Signal Temporal Logic (STL) specifications' \
        + ' against informal textual requirements.',
    long_description=README,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
    ],
    url='https://github.com/STLInspector/STLInspector',
    author='Eva Charlotte Mayer, Hendrik Roehm',
    author_email='eva-charlotte.mayer@posteo.de, git@roehm.ws',
    license='Apache License 2.0',
    packages=['STLInspector'],
    install_requires=[
        'markdown',
        'flask',
        'flask_assets',
        'antlr4-python2-runtime',
        'z3-solver'
    ],
    entry_points={
        'console_scripts': ['stlinspector=STLInspector.command_line:main'],
    },
    include_package_data=True,
    zip_safe=False)
