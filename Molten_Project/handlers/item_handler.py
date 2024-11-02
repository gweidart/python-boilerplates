from molten import Handler

class ItemHandler(Handler):
    def get(self, item_id):
        return {'item_id': item_id, 'name': 'Item Name', 'description': 'Item Description'}
