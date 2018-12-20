# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2018/12/15 16:37

from flask import Flask
from app.api.v1 import create_blueprint_v1


# 注册蓝图
def register_blueprints(app):
    app.register_blueprint(create_blueprint_v1(), url_prefix="/v1")


# 注册插件
def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    # with app.app_context():
    #     db.create_all()


def create_app():
    app = Flask(__name__)

    app.config.from_object("app.config.setting")
    app.config.from_object("app.config.secure")

    register_blueprints(app)
    register_plugin(app)

    return app



