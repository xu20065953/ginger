# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2018/12/15 18:42

from enum import Enum


# 客户端类型枚举
class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201


