from japronto import Application

app = Application()

@app.route('/')
def index(request):
    return request.response.text('Welcome to Japronto!')

if __name__ == '__main__':
    app.run(debug=True)
