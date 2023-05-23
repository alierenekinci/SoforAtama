import inspect
import json

from flask import request
from sqlalchemy import func

from db import db


def filtrele(db_sinifi):
    sorgu = db.session.query(db_sinifi)
    if 'sorgu' in request.args:
        talep = request.args['sorgu']
        talep_objesi = json.loads(talep)

        sinif_degiskenleri = dict(inspect.getmembers(db_sinifi))

        for alan in talep_objesi:
            if alan == "sirala":
                alanlar = talep_objesi[alan].split(",")
                for s_alan in alanlar:
                    if s_alan.startswith("-"):
                        sorgu = sorgu.order_by(sinif_degiskenleri[s_alan[1:]].desc())
                    elif s_alan.startswith("+"):
                        sorgu = sorgu.order_by(sinif_degiskenleri[s_alan[1:]].asc())
                    else:
                        sorgu = sorgu.order_by(sinif_degiskenleri[s_alan])
            else:
                db_alani = sinif_degiskenleri[alan]
                deger = talep_objesi[alan]
                if deger.startswith(">="):
                    sorgu = sorgu.filter(db_alani >= deger[2:])
                elif deger.startswith(">"):
                    sorgu = sorgu.filter(db_alani > deger[1:])
                else:
                    sorgu = sorgu.filter(func.lower(db_alani) == talep_objesi[alan].lower())

    return sorgu
