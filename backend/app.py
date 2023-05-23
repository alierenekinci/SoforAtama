import os

from dotenv import load_dotenv
from flask import Flask

from api import api
from db import *
from export import ma

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URL")

db.init_app(app)
ma.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run()
