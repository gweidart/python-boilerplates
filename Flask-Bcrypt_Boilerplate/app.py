from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    return jsonify({'username': username, 'hashed_password': hashed_password}), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    # Here, you'd typically fetch the hashed password from your database
    # For demonstration purposes, we'll use a dummy hashed password
    stored_hashed_password = bcrypt.generate_password_hash('mypassword').decode('utf-8')

    if bcrypt.check_password_hash(stored_hashed_password, password):
        return jsonify({'message': f'Welcome, {username}!'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)
