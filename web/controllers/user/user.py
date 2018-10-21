# -*- coding:utf-8 -*-
__author__ = 'Administrator'
from flask import Blueprint

route_user = Blueprint('user_page',__name__)

@route_user.route('/login')
def login():
    return 'login'
