import tornado.ioloop
import tornado.web
from handlers.main import MainHandler

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Tornado server running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
