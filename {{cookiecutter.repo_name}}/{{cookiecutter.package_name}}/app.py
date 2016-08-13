# -*- coding: utf-8 -*-
"""
    {{cookiecutter.package_name}}.app
    {{(cookiecutter.package_name + ".app") | length * '~'}}
"""

import simplejson as json
from flask import Flask
from {{cookiecutter.package_name}}.config import DevConfig
from {{cookiecutter.package_name}}.extensions import register_extensions


class Application(Flask):

    json_decoder = json.JSONDecoder
    json_encoder = json.JSONEncoder


def create_app(config_object=DevConfig):
    """Creates the application instance and calls the extension initializers.
    """
    app = Application(__name__)
    app.config.from_object(config_object)

    register_extensions(app)

    return app
