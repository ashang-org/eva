from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

import eva.utils.db

ORMBase = declarative_base()

# http://docs.sqlalchemy.org/en/latest/orm/contextual.html
# http://docs.sqlalchemy.org/en/latest/orm/session_basics.html#session-faq-whentocreate


def get_db_session():

    DB_URI = eva.utils.db.get_db_uri()
    dbengine = create_engine(DB_URI, echo=False)
    session_factory = sessionmaker(bind=dbengine)
    Session = scoped_session(session_factory)

    return Session


def get_db():
    db_session = get_db_session()
    return db_session()


def create_all(echo=False):

    DB_URI = eva.utils.db.get_db_uri()
    dbengine = create_engine(DB_URI, echo=echo)
    ORMBase.metadata.create_all(dbengine)
    dbengine.dispose()


def drop_all(echo=False):

    DB_URI = eva.utils.db.get_db_uri()
    dbengine = create_engine(DB_URI, echo=echo)
    ORMBase.metadata.drop_all(dbengine)
    dbengine.dispose()
