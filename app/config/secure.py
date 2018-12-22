# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2018/12/15 16:42

# jsonify 返回数据支持中文
JSON_AS_ASCII = False


SQLALCHEMY_DATABASE_URI = "mysql+cymysql://root:1234+abcd@localhost:3306/ginger"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True
SECRET_KEY = '\x12\x03\xc1\xcd0\xee_2\xfe\x9b\xd0\xff\xaf;\xddD\xa9%\xcc|<\xc8"\xd9'

# token 过期时间
TOKEN_EXPIRATION = 24 * 3600