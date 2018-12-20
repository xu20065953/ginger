# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2018/12/15 19:15

from flask import url_for, request, jsonify

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import CustomError, Success
from app.libs.redprint import Redprint
from app.models.base import db
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint("client")


@api.route("/register", methods=["POST"])
def create_client():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()
    return Success()

    # form = ClientForm(data=request.json)
    # if form.validate():
    #     promise = {
    #         ClientTypeEnum.USER_EMAIL: __register_user_by_email
    #     }
    #     promise[form.type.data]()
    #     return "success"
    # else:
    #     raise CustomError(form_errors=form.errors)
    # return "create client" + url_for("v1.useruser_create")


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
    # if form.validate():
    #     User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
    # else:
    #     raise CustomError(form_errors=form.errors, error_code=1005)




