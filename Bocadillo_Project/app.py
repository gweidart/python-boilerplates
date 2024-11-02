from bocadillo import App

app = App()

@app.route('/')
async def index(request):
    return 'Welcome to Bocadillo!'

if __name__ == '__main__':
    app.run(debug=True)
