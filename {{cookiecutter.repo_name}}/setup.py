# -*- coding: utf-8 -*-
"""
"""

from setuptools import setup

VERSION = '{{cookiecutter.version}}'

setup(
    name='{{cookiecutter.package_name}}',
    version=VERSION,
    url='http://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}',
    license='{{cookiecutter.license}}',
    author=u'{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    description='{{cookiecutter.project_short_description}}',
    packages=['{{cookiecutter.package_name}}'],
    install_requires=[
        'simplejson',
        'PyMySQL',
        'Flask>=0.10.1',
        'Flask-Bcrypt',
        'Flask-DebugToolbar',
        'Flask-Script',
        'Flask-API',
        'Flask-Marshmallow',
        'Flask-SQLAlchemy',
        'Flask-Migrate',
        'marshmallow-sqlalchemy',
    ],
    test_suite='tests',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Framework :: Flask',
        'License :: OSI Approved :: MIT License'
    ]
)
