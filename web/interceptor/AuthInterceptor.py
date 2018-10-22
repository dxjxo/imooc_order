# -*- coding:utf-8 -*-
__author__ = 'Administrator'
from application import app
from flask import request,redirect
from common .models.user import User
from common.libs.user.UserService import UserService
from common.libs.UrlManager import UrlManager
import re
#加上这个装饰品，就会对到达controlls层的所有请求 进行先拦截
@app.before_request
def before_request():
    igonre_urls = app.config["IGNORE_URLS"] #IGNORE_URLS ,IGNORE_CHECK_LOGIN_URLS 配置在 base_setting.py文件中
    igonre_check_login_urls = app.config["IGNORE_CHECK_LOGIN_URLS"]

    # 对以/static 开始 的静态文件 请求链接 都 进行过滤 不 进行登陆下面的登陆检查
    pattern = re.compile('%s'% "|".join(igonre_check_login_urls))
    path = request.path
    if pattern.match(path):
        return

    # 对以登陆页面 进行过滤 不 进行下面的登陆检查
    pattern = re.compile('%s' % "|".join(igonre_urls))
    path = request.path
    if pattern.match(path):
        return

    user_info = check_login()

    if not user_info:
        return  redirect(UrlManager.buildUrl('/user/login'))
    return


'''
判断用户是否登陆
'''
def check_login():
    cookies = request.cookies
    auth_cookie = cookies[app.config['AUTH_COOKIE_NAME']] if app.config['AUTH_COOKIE_NAME'] in cookies else None

   # 以上所有判断 都是 判断cookie是否篡改过 或者 有没有cookie
    if auth_cookie is None:
        return  False
    auth_info = auth_cookie.split('#')
    print("...............",auth_info)
    if len(auth_info) != 2:  # cookie 形状 08c7f742cb1750f54b532d989bf3e069#1
        return False

    try:
        user_info = User.query.filter_by(uid = auth_info[1]).first()
    except Exception :
        return False

    if user_info is None:
        return False
    if auth_info[0] != UserService.genAuthCode(user_info):
        return False
    return  user_info
