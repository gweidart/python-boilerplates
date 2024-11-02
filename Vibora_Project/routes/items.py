from vibora import Route

async def item_route(request):
    return 'Item route!'

app.add_route(Route('/items', item_route, methods=['GET']))
