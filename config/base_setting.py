#SERVER_PORT = 8000
SQLALCHEMY_ECHO = False #将所有的sql语句不打印出出来
DEBUG = False



# 过滤URL     c即与拦截器进行使用
IGNORE_URLS = {
    "^/user/login"

}
IGNORE_CHECK_LOGIN_URLS ={
    "^/static",
    "^/favicon.icon"
}

PAGE_SIZE = 50
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    "1":"正常",
    "0":"已删除"
}