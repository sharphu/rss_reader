#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os

from flask import Flask
from rss_reader.config import Config
from rss_reader.models import db
from rss_reader.views import bp_api, bp_home, bp_rss


def create_app():
    app = Flask(__name__)
    db_path = os.path.join(Config.BASE_DIR, 'models/rss_reader.db')
    app.register_blueprint(bp_api)
    app.register_blueprint(bp_home)
    app.register_blueprint(bp_rss)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['SECRET_KEY'] = 'you - will - never - guess'
    db.init_app(app)
    db.create_all(app=app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=Config.DEBUG)
