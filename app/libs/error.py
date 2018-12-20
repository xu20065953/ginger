# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2018/12/20 13:56
from flask import request, json
from werkzeug.exceptions import HTTPException


class ApiException(HTTPException):
    code = 500
    msg = "sorry we made a mistake"
    form_msg = None
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None, form_msg=None, headers=None):
        if msg:
            self.msg = msg
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if form_msg:
            self.form_msg = form_msg
        super(ApiException, self).__init__(msg, None)

    # 重写get_body方法
    def get_body(self, environ=None):
        """Get the HTML body."""
        body = dict(
            msg=self.msg,
            # form_msg=self.form_msg,
            error_code=self.error_code,
            request=request.method + " " + self.get_url_no_param()
        )
        return json.dumps(body)

    # 重写get_headers方法
    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]


    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split("?")
        return main_path[0]



