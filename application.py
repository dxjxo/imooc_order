# -*- coding:utf-8 -*-
__author__ = 'Administrator'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import  Manager
import os
class Application(Flask):
    def __init__(self,import_name,template_folder=None,root_path=None):
        super(Application,self).__init__(import_name,template_folder=template_folder,root_path=root_path,static_folder=None)
        self.config.from_pyfile('config/base_setting.py')
        #定义一个‘ops_config’环境变量 ， 在linux命令行下 用 export ops_config = local , 那么下面的语句就是加载local_setting.py配置文件
        if 'ops_config' in os.environ:
            self.config.from_pyfile('config/%s_setting.py'%os.environ['ops_config'])
        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__,template_folder=os.getcwd()+'/web/templates/',root_path=os.getcwd())
app.config['JSON_AS_ASCII'] = False  #是支持用jsonify返回json数据时   支持中文显示
manager = Manager(app)

'''
函数模板 ，即py文件中的静态方法，可以龙html模板中调用 (如/common/layout_user.html", line 9)
'''
from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildStaticUrl,'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl,'buildUrl')