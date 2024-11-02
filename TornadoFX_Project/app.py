from tornado import web, ioloop

class MainHandler(web.RequestHandler):
    def get(self):
        self.write("Welcome to TornadoFX!")

def make_app():
    return web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    ioloop.IOLoop.current().start()
