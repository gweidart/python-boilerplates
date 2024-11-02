from robyn import Robyn

app = Robyn()

@app.get('/')
async def index():
    return 'Welcome to Robyn!'

if __name__ == '__main__':
    app.run(debug=True)
