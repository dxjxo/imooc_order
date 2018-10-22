# -*- coding:utf-8 -*-
__author__ = 'Administrator'
from flask import Blueprint,render_template,request ,jsonify,make_response
from common.models.user import User
from common.libs.user.UserService import UserService
<<<<<<< HEAD
import json
from application import  app
=======
>>>>>>> 2946b1dc0f9d39feeffaa7223f4741c010933b2b
route_user = Blueprint('user_page',__name__)

@route_user.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('user/login.html')

    resp = {'code':200,'msg':'登陆成功','data':{}}
    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''
    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入用户名'
        return jsonify(resp)

    if login_pwd is None or len(login_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入密码'
        return jsonify(resp)

    user_info = User.query.filter_by(login_name = login_name).first()
    if not user_info:
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名'
        return jsonify(resp)
    # 判断密码
    if user_info.login_pwd != UserService.genPwd(login_pwd,user_info.login_salt):
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名密码'
        return jsonify(resp)
<<<<<<< HEAD
    from flask import make_response
    response = make_response(json.dumps(resp))
    #  生成cookie并加密
    response.set_cookie(app.config['AUTH_COOKIE_NAME'],"%s#%s"%(UserService.genAuthCode(user_info),user_info.uid))
    #return jsonify(resp)
    return  response
=======

    return jsonify(resp)
>>>>>>> 2946b1dc0f9d39feeffaa7223f4741c010933b2b


@route_user.route('/edit')
def edit():
    return render_template('user/edit.html')
@route_user.route('/reset-pwd')
def reset_pwd():
    return render_template('user/reset_pwd.html')