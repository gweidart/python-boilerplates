from esmerald import Esmerald

app = Esmerald()

@app.get('/')
async def index():
    return 'Welcome to Esmerald!'

if __name__ == '__main__':
    app.run(debug=True)
