from flask import Blueprint

from db import Sofor, Otobus, Sefer, Hat, Atama
from export.semalar import SeferSema, OtobusSema, SoforSema, HatSema, AtamaSema
from .public_endpoints import genel_endpoint_olustur

v1 = Blueprint('v1', __name__)

v1.register_blueprint(genel_endpoint_olustur('sofor', Sofor, SoforSema), url_prefix='/sofor')
v1.register_blueprint(genel_endpoint_olustur('otobus', Otobus, OtobusSema), url_prefix='/otobus')
v1.register_blueprint(genel_endpoint_olustur('sefer', Sefer, SeferSema), url_prefix='/sefer')
v1.register_blueprint(genel_endpoint_olustur('hat', Hat, HatSema), url_prefix='/hat')
v1.register_blueprint(genel_endpoint_olustur('atama', Atama, AtamaSema), url_prefix='/atama/')

api = Blueprint('api', __name__)
api.register_blueprint(v1, url_prefix='/v1')

