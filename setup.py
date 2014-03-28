#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='simplehttp',
      version='1.1',
      description='Super simple threaded web server for development',
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Topic :: Internet :: WWW/HTTP",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   'Programming Language :: Python',
                   "Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.3",
                   ],
      license='BSD',
      author='Joshua D. Boyd',
      author_email='jdboyd@jdboyd.net',
      scripts=['simplehttp.py'],
      entry_points = {'console_scripts': ['simplehttp = simplehttp:run']}
     )
