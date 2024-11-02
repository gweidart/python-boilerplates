import falcon

app = falcon.App()

@app.route('/')
def index(req, resp):
    resp.media = {'message': 'Welcome to Falconry!'}

if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
