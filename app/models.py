from . import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text)
    num_bedrooms = db.Column(db.Integer)
    num_bathrooms = db.Column(db.Integer)
    price = db.Column(db.Float)
    p_type = db.Column(db.String(80))
    location = db.Column(db.String(120))
    photo = db.Column(db.)