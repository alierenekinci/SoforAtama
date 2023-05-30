from db.baglanti import db


class Sefer(db.Model):
    sefer_id = db.Column(db.Integer, primary_key = True)
    sefer_tarih = db.Column(db.String(150))
    sefer_saat = db.Column(db.String(150))
    hat_id = db.Column(db.Integer, db.ForeignKey('hat.hat_id'))
    otobus_id = db.Column(db.Integer, db.ForeignKey('otobus.otobus_id'))

    # sofor eklenecek
    # Burada relationshipte eksik var.


    # Gerekmiyor bile olabilir.
    hat = db.relationship('Hat', backref = 'seferler')
    #otobus = db.relationship(Otobus, backref = 'seferler')