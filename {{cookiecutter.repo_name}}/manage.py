#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

from flask_script import Manager, Server, Shell
from flask_script.commands import ShowUrls
from flask_migrate import MigrateCommand

from {{cookiecutter.package_name}}.app import create_app
from {{cookiecutter.package_name}}.extensions import db

app = create_app()
manager = Manager(app)

def _make_context():
    return {'app': app, 'db': db}

manager.add_command('serve', Server)
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)
manager.add_command('urls', ShowUrls())

if __name__ == '__main__':
    manager.run()
