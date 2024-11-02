from esmerald import Esmerald

app = Esmerald()

@app.get('/items')
async def items():
    return 'Items route!'
