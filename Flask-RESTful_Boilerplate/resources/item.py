from flask_restful import Resource

class ItemResource(Resource):
    def get(self, name):
        return {'item': name, 'message': 'This is a sample item resource'}
