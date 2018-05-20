#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, DateTime
from sqlalchemy import Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from passlib.apps import custom_app_context as pwd_context
from datetime import datetime
from .resource import get_unique_str
from .settings import db

Base = declarative_base()
secret_key = get_unique_str(32)

# prepare engine
connect = 'postgresql://{}:{}@{}/{}'.format(db['user'],
                                            db['password'],
                                            db['host'],
                                            db['database'])


# create session
engine = create_engine(connect)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class User(Base):
    __tablename__ = 'user'
    id = Column('id', Integer, primary_key=True)
    first_name = Column('first_name', String(60))
    last_name = Column('last_name', String(60))
    email = Column('email', String(45))
    hash = Column('hash', String(250))
    is_active = Column('is_active', Boolean, default=False)
    last_visit = Column('last_visit', DateTime, onupdate=datetime.utcnow)
    register_date = Column('register_date', DateTime)
    is_staff = Column('is_staff', Boolean, default=False)
    is_super_user = Column('is_super_user', Boolean, default=False)

    def hash_password(self, password):
        """
        Get string and hashing it

        :param password: (str)
        :return void:
        """
        self.hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        """
        Password verification

        :param password:
        :return bool:
        """
        return pwd_context.verify(password, self.hash)


# create an engine
engine = create_engine(connect)
Base.metadata.create_all(engine)
