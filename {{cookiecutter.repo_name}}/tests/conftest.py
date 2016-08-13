# -*- coding: utf-8 -*-

import pytest
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


@pytest.fixture
def engine():
    engine = sa.create_engine('sqlite:///:memory:')
    return engine


@pytest.fixture
def connection(engine):
    return engine.connect()


@pytest.fixture
def Base():
    return declarative_base()


@pytest.fixture
def init_models():
    pass


@pytest.fixture
def session(request, engine, connection, Base, init_models):
    sa.orm.configure_mappers()
    Base.metadata.create_all(connection)
    Session = sessionmaker(bind=connection)
    session = Session()

    def teardown():
        session.close_all()
        Base.metadata.drop_all(connection)
        connection.close()
        engine.dispose()

    request.addfinalizer(teardown)

    return session
