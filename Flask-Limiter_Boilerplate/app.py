from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["5 per minute"]
)

@app.route('/')
@limiter.limit("2 per minute")
def index():
    response = {'message': 'This route is limited to 2 requests per minute.'}
    return jsonify(response)

@app.route('/slow')
@limiter.limit("1 per minute")
def slow_route():
    response = {'message': 'This route is limited to 1 request per minute.'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
