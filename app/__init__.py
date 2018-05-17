#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, g, make_response

from flask_httpauth import HTTPBasicAuth

from settings import BASE_DIR

# define global variables
app = Flask(__name__)
auth = HTTPBasicAuth()


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
