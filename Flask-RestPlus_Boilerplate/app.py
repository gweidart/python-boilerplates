from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app, version='1.0', title='Flask-RestPlus API', description='A simple Flask-RestPlus API')

ns = api.namespace('items', description='Items operations')

items = []

@ns.route('/<string:name>')
class ItemResource(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item, 200
        return {'message': 'Item not found'}, 404

    def post(self, name):
        item = {'name': name, 'description': f'Description of {name}'}
        items.append(item)
        return item, 201

if __name__ == '__main__':
    app.run(debug=True)
