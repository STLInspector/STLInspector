"""generates a distribution file for pypi"""

import os
import pypandoc

#converts markdown to reStructured
readme_rst = pypandoc.convert('README.md', 'rst', format='markdown')

#writes converted file
with open('README', 'w') as rstfile:
    rstfile.write(readme_rst)

os.system("python setup.py sdist")
