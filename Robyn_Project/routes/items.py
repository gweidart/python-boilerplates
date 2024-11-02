from robyn import Robyn

app = Robyn()

@app.get('/items')
async def items():
    return 'Items route!'
