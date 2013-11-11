"""
    Flask-Scrypt
    ------------

    Flask-Scrypt flask extension provides scrypt password hashing and
    random salt generation.

    Links
    `````
    * `development version <https://github.com/grobins2/flask-scrypt>`_
"""
import os
from setuptools import setup

MODULE_PATH = os.path.join(os.path.dirname(__file__), 'flask_scrypt.py')
VERSION_LINE = [f for f in open(MODULE_PATH).readlines() 
        if '__version_info__' in f][0]

__version__ = '.'.join(eval(VERSION_LINE.split('__version_info__ = ')[-1]))


setup(name='Flask-Scrypt',
        description='Random salt generation and Scrypt password hashing for Flask.',
        version=__version__,
        url='http://github.com/grobins2/flask-scrypt',
        license='MIT',
        author='Gilbert Robinson',
        author_email='grobins2@gmail.com',
        long_description=__doc__,
        py_modules=['flask_scrypt'],
        platforms='any',
        install_requires=['Flask', 'scrypt'],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'Lisense :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules'
            ])
