from app import db

class User(db.Model):

    username = db.Column(db.String(50),primary_key=True , unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

