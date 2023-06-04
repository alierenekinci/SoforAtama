from db import Sofor, Otobus, Sefer, Hat, Atama
from export import ma


# Kayıt Ekleme ve Listeleme Şemaları
class SoforSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sofor
        load_instance=True


class OtobusSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Otobus
        load_instance = True


class SeferSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sefer
        include_fk = True
        load_instance = True


class HatSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Hat
        load_instance = True


class AtamaSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Atama
        load_instance = True
