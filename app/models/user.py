# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2018/12/15 18:31

from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.error_code import AuthFailed
from app.models.base import Base, db


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24))
    age = Column(Integer)
    auth = Column(SmallInteger, default=1)
    _password = Column("password", String(124))

    # 需要被序列化的字段
    def keys(self):
        return ['id', 'email', 'nickname', 'auth', 'age']

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    # 邮箱注册
    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

    # 验证邮箱和密码登录
    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first_or_404()
        if not user.check_password(password):
            raise AuthFailed()
        return {"uid": user.id, "scope": ""}

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)





