from db.baglanti import db

class Otobus(db.Model):
    otobus_id = db.Column(db.BigInteger, primary_key = True)
    otobus_tur = db.Column(db.String(150))#tür
    otobus_sayi = db.Column(db.BigInteger)