# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2018/12/20 15:25
from flask import request
from wtforms import Form
from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        super(BaseForm, self).__init__(data=request.json)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(self.errors)
        return self



