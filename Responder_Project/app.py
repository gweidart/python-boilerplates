from responder import Responder

api = Responder()

@api.route('/')
async def index(req, resp):
    resp.text = 'Welcome to Responder!'

if __name__ == '__main__':
    api.run()
