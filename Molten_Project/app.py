from molten import Molten

app = Molten()

@app.route('/')
def index():
    return {'message': 'Welcome to Molten!'}

if __name__ == '__main__':
    app.run(debug=True)
