from flask import Flask
from flask_restful import Api
from resources.item import ItemResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ItemResource, '/item/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)
