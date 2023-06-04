from db.baglanti import db

class Otobus(db.Model):
    otobus_id = db.Column(db.BigInteger, primary_key = True)
    otobus_plaka = db.Column(db.String(150))
    otobus_tur = db.Column(db.String(150))
    otobus_kapasite = db.Column(db.BigInteger)