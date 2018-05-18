#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, DateTime
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

# create an engine
engine = create_engine(connect)
Base.metadata.create_all(engine)
