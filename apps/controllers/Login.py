__author__ = 'Administrator'
import tornado.web

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
          self.render("login/login.html")

