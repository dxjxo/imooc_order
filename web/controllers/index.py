# -*- coding:utf-8 -*-
__author__ = 'Administrator'
from flask import  Blueprint

route_index  = Blueprint('index_page',__name__)
@route_index.route('/')
def index():
    return '搭建好了整个项目框架'