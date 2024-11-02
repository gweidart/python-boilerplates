from klein import Klein

app = Klein()

@app.route('/')
def index(request):
    return 'Welcome to Klein!'

if __name__ == '__main__':
    app.run(debug=True)
