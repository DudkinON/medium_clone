#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from os import path
from .keys import user_name, user_password, database_name, host

BASE_DIR = path.dirname(path.realpath(__file__))

db = {
    'user': user_name,
    'password': user_password,
    'database': database_name,
    'host': host
}