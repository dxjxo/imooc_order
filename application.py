# -*- coding:utf-8 -*-
__author__ = 'Administrator'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import  Manager
import os
class Application(Flask):
    def __init__(self,import_name):
        super(Application,self).__init__(import_name)
        self.config.from_pyfile('config/local_setting.py')
        #定义一个‘ops_config’环境变量 ， 在linux命令行下 用 export ops_config = local , 那么下面的语句就是加载local_setting.py配置文件
        if 'ops_config' in os.environ:
            self.config.from_pyfile('config/%s_setting.py'%os.environ['ops_config'])
        db.init_app(self)


db = SQLAlchemy()
app = Flask(__name__)
manager = Manager(app)

