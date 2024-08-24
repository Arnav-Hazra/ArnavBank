import tornado.ioloop
import tornado.web
from register import Register
from formhandler import FormHandler
from transactionhandler import TransactionHandler
from gettransaction import GetTransaction
from getbalance import GetBalance

register = Register()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Bank Transaction Register")


def make_app():
    return tornado.web.Application([
        (r"/v1", FormHandler),
        (r"/v1/addtransaction", TransactionHandler, dict(register = register)),
        (r"/v1/gettransaction", GetTransaction, dict(register = register)),
        (r"/v1/checkbalance", GetBalance, dict(register = register)),
        ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
