# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2018/12/15 16:59
from flask import jsonify, g, render_template

from app.libs.error_code import DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = Redprint("user")


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    # r = {
    #     "id": user.id,
    #     "nickname": user.nickname,
    #     "email": user.email
    # }
    return jsonify(user)


# 注销用户自己
@api.route("/delete", methods=["POST"])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid, status=1).first_or_404()
        user.delete()
    return DeleteSuccess()


@api.route("/test")
def test():
    return render_template("test.html")

