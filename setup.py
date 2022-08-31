#!/usr/bin/env python

from distutils.core import setup
from setuptools import setup, find_packages

setup(name='Date2Vec',
      version='1.0',
      description='Pretrained models and scripts to train new models to get embeddings of Time-Date data',
      author='Surya Kant Sahu',
      author_email='surya.oju@gmail.com',
      url='https://github.com/ojus1/Date2Vec',
      packages=find_packages(),
      package_dir = {'': '.'}
     )
