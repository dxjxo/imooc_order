# -*- coding:utf-8 -*-
__author__ = 'Administrator'
import hashlib,base64,string,random
class UserService():
    """
    对cookie加密
    对用户输入的密码加上随机字符串进行 md5 和 base64 加密
    """
    @staticmethod
    def genAuthCode(user_info):
        m = hashlib.md5()
        str = "%s-%s-%s-%s" % (user_info.uid,user_info.login_name,user_info.login_pwd,user_info.login_salt)
        m.update(str.encode('utf-8'))
        return m.hexdigest()  # 返回16进制

    @staticmethod
    def genPwd(pwd,salt):
        # 初始化md5
        m = hashlib.md5()
        str = "%s-%s" %(base64.encodebytes(pwd.encode("utf-8")),salt)
        m.update( str.encode('utf-8') )
        return m.hexdigest()# 返回16进制

    @staticmethod
    def geneSalt(length=16):
        keylist = [random.choice((string.ascii_letters + string.digits)) for i in range(length)]
        return ("".join(keylist))
