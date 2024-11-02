from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Flask-RESTX API', description='A simple Flask-RESTX API')

ns = api.namespace('items', description='Items operations')

item_model = api.model('Item', {
    'name': fields.String(required=True, description='The name of the item'),
    'description': fields.String(required=True, description='The description of the item')
})

items = []

@ns.route('/<string:name>')
@ns.response(404, 'Item not found')
@ns.param('name', 'The item identifier')
class ItemResource(Resource):
    @ns.doc('get_item')
    @ns.marshal_with(item_model)
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        api.abort(404, "Item not found")

    @ns.doc('create_item')
    @ns.expect(item_model)
    @ns.marshal_with(item_model, code=201)
    def post(self, name):
        item = {'name': name, 'description': f'Description of {name}'}
        items.append(item)
        return item, 201

if __name__ == '__main__':
    app.run(debug=True)
