# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2018/12/15 19:15

from flask import url_for
from app.libs.redprint import Redprint

api = Redprint("client")


@api.route("/register", methods=["POST"])
def create_client():
    return "create client" + url_for("v1.useruser_create")






