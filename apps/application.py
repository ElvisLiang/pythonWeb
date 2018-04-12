from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado import httpserver
from controllers.Login import LoginHandler
import tornado

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.redirect("")

settings = {
    'template_path': 'views',
    'cookie_secret': 'asdfpojaksdfyknasdfklasdf',
     'static_path': 'static',
     'static_url_prefix': '/static/',
}



application = tornado.web.Application([
(r"/main",MainHandler),
(r"/login",LoginHandler),
],**settings)

if __name__ == "__main__":
    application.listen("8080")
    tornado.ioloop.IOLoop.instance().start()
