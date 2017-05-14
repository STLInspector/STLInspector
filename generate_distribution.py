"""
generates a distribution file for pypi

workflow:
1. execute this file
2. install the generated package locally
3. check that it works
4. upload the package
"""

import os
import pypandoc

#converts markdown to reStructured
readme_rst = pypandoc.convert('README.md', 'rst', format='markdown')

#writes converted file
with open('README', 'w') as rstfile:
    rstfile.write(readme_rst)

os.system("python setup.py sdist")
