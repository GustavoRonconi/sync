from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import configparser

"""Importa a configuração da aplicação"""
configuration = configparser.RawConfigParser()
configuration.read("sync/application.config")


DATA_BASE_URI = configuration.get("DATABASE", "DATABASE_URI")
engine = create_engine(DATA_BASE_URI, convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models

    Base.metadata.create_all(bind=engine)
