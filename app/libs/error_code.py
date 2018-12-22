# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2018/12/20 11:30

from werkzeug.exceptions import HTTPException
from app.libs.error import ApiException


class CustomError(ApiException):
    code = 400
    # description = "客户端注册类型(type参数)错误"
    msg = None
    form_msg = None
    error_code = 1001

    def __init__(self, msg=None, error_code=None, form_errors=None):
        if msg:
            self.msg = msg
        if error_code:
            self.error_code = error_code
        if form_errors:
            s = ""
            for k, v in form_errors.items():
                if s:
                    s += "\n"
                s += k + ": " + "".join(v)
            self.form_msg = s
        super(CustomError, self).__init__()


class ParameterException(ApiException):
    code = 400
    msg = "参数错误"
    error_code = 1000


class Success(ApiException):
    code = 201
    msg = "ok"
    error_code = 1


class DeleteSuccess(Success):
    code = 202
    msg = "ok"
    error_code = 0


class ServerError(ApiException):
    code = 500
    msg = 'sorry, 发生了一些未知的错误!'
    error_code = 999


class AuthFailed(ApiException):
    code = 401
    msg = '未授权...'
    error_code = 1005


class NotFound(ApiException):
    code = 404
    msg = 'the resource are not found O__O...'
    error_code = 1001

