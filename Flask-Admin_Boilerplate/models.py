from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SampleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))

    def __repr__(self):
        return f'<SampleModel {self.name}>'
