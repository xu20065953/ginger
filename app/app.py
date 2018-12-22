# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2018/12/15 16:39
from datetime import date

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from app.libs.error_code import ServerError


# 重写Flask json序列化方法
class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()


# 重写Flask 对象 覆盖json_encoder
class Flask(_Flask):
    json_encoder = JSONEncoder

