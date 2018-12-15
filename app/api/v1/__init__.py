# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2018/12/15 17:12

from flask import Blueprint
from app.api.v1 import user, client


def create_blueprint_v1():
    blueprint_v1 = Blueprint("v1", __name__)

    user.api.register(blueprint_v1, url_prefix="/user")
    client.api.register(blueprint_v1, url_prefix="/client")

    return blueprint_v1






