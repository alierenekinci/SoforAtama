from db import Sofor, Otobus, Sefer, Hat
from export import ma


#Kayıt Ekleme ve Listeleme Şemaları
class SoforSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sofor

class OtobusSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Otobus

class SeferSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sefer
        include_fk = True

class HatSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Hat
