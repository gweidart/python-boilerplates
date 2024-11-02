import cyclone.web
from cyclone import ioloop

class MainHandler(cyclone.web.RequestHandler):
    def get(self):
        self.write("Welcome to Cyclone!")

def make_app():
    return cyclone.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    ioloop.IOLoop.current().start()
