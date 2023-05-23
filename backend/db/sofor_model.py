from db.baglanti import db

class Sofor(db.Model):
    sofor_id = db.Column(db.BigInteger, primary_key = True)
    sofor_ad = db.Column(db.String(150))
    sofor_soyad = db.Column(db.String(150))
    cinsiyet = db.Column(db.String(150))