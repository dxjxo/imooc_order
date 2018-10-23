# -*- coding:utf-8 -*-
__author__ = 'Administrator'
# -*- coding:utf-8 -*-
__author__ = 'Administrator'
import hashlib,requests,string,random,json
from application import  app

class MemberService():

    @staticmethod
    def geneAuthCode(member_info=None):
        m = hashlib.md5()
        str = "%s-%s-%s" % (member_info.id,member_info.salt,member_info.status)
        m.update(str.encode('utf-8'))
        return m.hexdigest()  # 返回16进制



    @staticmethod
    def geneSalt(length=16):
        keylist = [random.choice((string.ascii_letters + string.digits)) for i in range(length)]
        return ("".join(keylist))
    @staticmethod
    def getWeChatOpenId(code):
        print('code .....',code)

        url = "https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code" \
            .format(app.config['MINA_APP']['appid'], app.config['MINA_APP']['appkey'], code)


        r = requests.get(url)
        res = json.loads(r.text)

        openid = None
        if 'openid' in res:
            openid = res['openid']

        return  openid