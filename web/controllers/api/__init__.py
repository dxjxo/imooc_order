# -*- coding:utf-8 -*-
__author__ = 'Administrator'

"""
主要有用于小程序的API
"""

from flask import Blueprint

route_api = Blueprint('route_api',__name__)

@route_api.route('/')
def index():
    return 'mina api v1.0'