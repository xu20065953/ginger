# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2018/12/22 14:39
from flask import current_app, jsonify
from app.libs.enums import ClientTypeEnum
from app.libs.error_code import AuthFailed
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, TokenForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature

api = Redprint("token")


# 登录 获取token
@api.route("", methods=["POST"])
def create_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify,
    }
    identity = promise[form.type.data](form.account.data, form.secret.data)
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity["uid"], form.type.data, identity["scope"], expiration)
    t = {
        "token": token.decode("ascii")
    }
    return jsonify(t), 201


@api.route("/secret", methods=["POST"])
def get_token_info():
    form = TokenForm().validate_for_api()
    s = Serializer(current_app.config["SECRET_KEY"])
    try:
        data = s.loads(form.token.data)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired', error_code=1003)
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)

    r = {
        'scope': data[0]['scope'],
        'create_at': data[1]['iat'],
        'expire_in': data[1]['exp'],
        'uid': data[0]['uid']
    }
    return jsonify(r)


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    """生成Token令牌"""
    s = Serializer(current_app.config["SECRET_KEY"], expires_in=expiration)
    return s.dumps({
        "uid": uid,
        "type": ac_type.value,
        "scope": scope
    })




