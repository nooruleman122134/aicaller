from db import db

class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50))
    issue = db.Column(db.String(100))
