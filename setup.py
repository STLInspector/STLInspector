from setuptools import setup

setup(name='STLInspector',
    version='1.0.1',
    description='Systematic validation of Signal Temporal Logic (STL) specifications against informal textual requirements.',
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
    entry_points = {
        'console_scripts': ['stlinspector=STLInspector.command_line:main'],
    },
    include_package_data=True,
    zip_safe=False)
