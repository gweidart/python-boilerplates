from vibora import Vibora

app = Vibora()

@app.route('/')
async def index(request):
    return 'Welcome to Vibora!'

if __name__ == '__main__':
    app.run(debug=True)
