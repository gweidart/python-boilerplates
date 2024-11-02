from blacksheep import Application

app = Application()

@app.get('/')
async def index():
    return 'Welcome to BlackSheep!'

if __name__ == '__main__':
    app.start()
