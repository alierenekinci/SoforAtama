from urllib import request

from flask import Blueprint, jsonify

from aracgerec.filtreleme import filtrele
from db import db


def genel_endpoint_olustur(isim, db_sinifi, sema_sinifi):
    bp = Blueprint(isim, __name__)

    @bp.route('/', methods=['GET'])
    def listele():
        kayitlar = filtrele(db_sinifi).all()
        sema = sema_sinifi()
        return sema.dump(kayitlar, many=True)

    @bp.route('/sayfa/<int:kayit_sayisi>/<int:sayfa_no>')
    def sayfalama(kayit_sayisi, sayfa_no):
        sayfa_no -= 1

        atlanacak_kayit_sayisi = kayit_sayisi * sayfa_no
        getirilecek_kayit_sayisi = kayit_sayisi

        kayitlar = filtrele(db_sinifi).limit(getirilecek_kayit_sayisi).offset(atlanacak_kayit_sayisi)

        sema = sema_sinifi()
        return sema.dump(kayitlar, many=True)

    @bp.route("/sayfa/<int:kayit_sayisi>")
    def sayfa_sayisi(kayit_sayisi):
        atama_sayisi = filtrele(db_sinifi).count()

        sayfa_sayisi = atama_sayisi // kayit_sayisi

        if atama_sayisi % kayit_sayisi > 0:
            sayfa_sayisi += 1

        return jsonify({
            "kayit_sayisi": atama_sayisi,
            "sayfa_sayisi": sayfa_sayisi
        })

    @bp.route("/<int:id>", methods=["GET"])
    def detay(id):
        atama = db.get_or_404(db_sinifi, id)
        sema = sema_sinifi()
        return sema.dump(atama)

    @bp.route("/", methods=["POST"])
    def ekle():
        yeni_kayit = request.json
        yeni = db_sinifi(**yeni_kayit)
        db.session.add(yeni)
        db.session.commit()
        sema = sema_sinifi()
        return sema.dump(yeni)

    @bp.route("/<int:id>", methods=["PUT", "PATCH"])
    def guncelle(id):
        kayit = db.get_or_404(db_sinifi, id)
        kayit_bilgileri = request.json
        sema = sema_sinifi()
        guncel_kayit = sema.load(kayit_bilgileri, instance=kayit, session=db.session)
        db.session.commit()
        return sema.dump(guncel_kayit)

    @bp.route("/<int:id>", methods=["DELETE"])
    def sil(id):
        kayit = db.get_or_404(db_sinifi, id)
        db.session.delete(kayit)
        db.session.commit()
        return jsonify({"sonuc": "TAMAM"})

    return bp