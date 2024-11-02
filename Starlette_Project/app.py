from starlette.applications import Starlette
from starlette.responses import PlainTextResponse

app = Starlette()

@app.route('/')
async def homepage(request):
    return PlainTextResponse('Welcome to Starlette!')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level="info")
