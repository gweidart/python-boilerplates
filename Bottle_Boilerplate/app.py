from bottle import Bottle, run, template, static_file

app = Bottle()

@app.route('/')
def home():
    return template('index')

@app.route('/static/<filename>')
def serve_static(filename):
    return static_file(filename, root='static/')

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
