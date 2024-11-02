from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    response = {'message': 'CORS is enabled for all domains!'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
