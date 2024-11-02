from starlette.routing import Route
from starlette.responses import PlainTextResponse

async def item_route(request):
    return PlainTextResponse('Item route!')

routes = [
    Route('/items', item_route),
]
