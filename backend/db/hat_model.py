from db.baglanti import db


class Hat(db.Model):
    hat_id = db.Column(db.Integer, primary_key = True)
    hat_ad = db.Column(db.String(150))
    hat_no = db.Column(db.String(150))