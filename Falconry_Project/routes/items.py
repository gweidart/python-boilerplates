import falcon

class ItemsResource:
    def on_get(self, req, resp):
        resp.media = {'items': ['Item 1', 'Item 2']}

app.add_route('/items', ItemsResource())
