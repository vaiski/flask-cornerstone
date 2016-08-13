# -*- coding: utf-8 -*-
"""
    {{cookiecutter.package_name}}.extensions
    {{(cookiecutter.package_name + ".extensions") | length * '~'}}

    Flask extensions used by the application.
"""

from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_debugtoolbar import DebugToolbarExtension

#pylint: disable=invalid-name
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)
bcrypt = Bcrypt()
migrate = Migrate()
ma = Marshmallow()
debug_toolbar = DebugToolbarExtension()


def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
