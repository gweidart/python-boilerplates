from aiohttp import web

async def items(request):
    return web.Response(text='Items route!')
