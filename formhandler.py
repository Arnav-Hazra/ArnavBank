import tornado.web

class FormHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/BankUI.html")
