# -*- coding:utf-8 -*-
__author__ = 'Administrator'
from application import app ,manager
from flask_script import Server
import www

#自取名
manager.add_command('runserver',Server(host='0.0.0.0',use_debugger=True,use_reloader=True))

def main():
    #app.run(host='0.0.0.0',debug=True)
    manager.run()
if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()
