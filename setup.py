from setuptools import setup, find_packages
import codecs
import os
import kiwifruit

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__),fname)).read()

long_desc = """
kiwifruit
===========
* my study tools for candlestick patten filter
"""

def read_install_requires():
    with open('requirements.txt','r') as f:
        res = f.readlines()
    res = list(map(lambda s: s.replace('\n',''),res))
    return res

setup(
    name='kiwifruit',
    version=kiwifruit.__version__,
    description='my study tool for candlestick pattern filter',
    long_description = long_desc,
    install_requires = read_install_requires(),
    author = 'Max Wu',
    author_email='maxwu3333@gmail.com',
    license='BSD',
    classifiers=['Development Status :: 4 - Beta',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'License :: OSI Approved :: BSD License'],
    packages=find_packages(),
    package_data={'': ['*.csv']},
)
