from db.baglanti import db

class Atama(db.Model):
    atama_id = db.Column(db.BigInteger, primary_key = True)
    atama_durum = db.Column(db.Boolean(), default= False)
    atama_tarih = db.Column(db.String(150))
    atama_gun = db.Column(db.Integer)
    atama_sonuc = db.Column(db.String(320000))