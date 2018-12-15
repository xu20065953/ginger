# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2018/12/15 16:59

from app.libs.redprint import Redprint
api = Redprint("user")


@api.route("/create")
def user_create():
    return "create user"

