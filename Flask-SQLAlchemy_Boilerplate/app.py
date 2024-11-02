from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import models after initializing db
import models

@app.route('/')
def index():
    return 'Welcome to the Flask-SQLAlchemy app!'

if __name__ == '__main__':
    app.run(debug=True)
