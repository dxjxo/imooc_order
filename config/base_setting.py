#SERVER_PORT = 8000
SQLALCHEMY_ECHO = False #将所有的sql语句不打印出出来
DEBUG = False



# 过滤URL     c即与拦截器进行使用
IGNORE_URLS = {
    "^/user/login",
    "^/api",

}
IGNORE_CHECK_LOGIN_URLS ={
    "^/static",
    "^/favicon.icon"
}
# 过滤掉 小程序的所有请求
API_IGNORE_URLS = [
    "^/api"
]

PAGE_SIZE = 50
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    "1":"正常",
    "0":"已删除"
}
MINA_APP = {
    'appid':'wx56761ceac8da8485',
    'appkey':'d3708f7f3e60bab15996bb911e1608a1'
}