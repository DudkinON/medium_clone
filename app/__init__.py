#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from flask import Flask, jsonify, g, make_response

from flask_httpauth import HTTPBasicAuth

from app.settings import BASE_DIR
from app.provider import *

# define global variables
app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(_login, password):
    
    user_id = User.verify_auth_token(_login)
    if user_id:
        user = get_user_by_id(user_id)
        if not user:
            return False
        if not get_user_by_id(user_id).verify_password(password):
            return False
    else:
        return False
    g.user = user
    return True


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
