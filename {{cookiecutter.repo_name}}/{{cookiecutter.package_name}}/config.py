# -*- coding: utf-8 -*-
"""
    {{cookiecutter.package_name}}.config
    {{(cookiecutter.package_name + ".config") | length * '~'}}

    Application configurations.
"""

import os


#pylint: disable=too-few-public-methods
class Config(object):
    """Application's base configuration."""

    APP_PATH = os.path.abspath(os.path.dirname(__file__))
    PROJECT_PATH = os.path.abspath(os.path.join(APP_PATH, os.pardir))
    SECRET_KEY = os.environ.get('{{cookiecutter.package_name | upper}}_SECRET', 'secret-key')
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////{0}/{1}'.format(
        Config.PROJECT_PATH, DB_NAME)


class TestConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    TESTING = True
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
