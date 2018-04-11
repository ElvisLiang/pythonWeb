from tornado.ioloop import IOLoop
from tornado.web import Application
import tornado

import tornado.ioloop
import tornado.web

class MainHandler():
    def get(self):
        self.redirect('http://www.baidu.com')



application = tornado.Application([



],)
