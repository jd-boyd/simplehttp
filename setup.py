#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='simplehttp',
      version='1.1',
      description='Super simple threaded web server',
      author='Joshua D. Boyd',
      author_email='jdboyd@jdboyd.net',
      scripts=['simplehttp.py'],
      entry_points = {'console_scripts': ['simplehttp = simplehttp:run']}
     )
