# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2018/12/15 16:54
from werkzeug.exceptions import HTTPException

from app import create_app
from app.libs.error import ApiException
from app.libs.error_code import ServerError

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, ApiException):
        return e
    elif isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return ApiException(msg=msg, code=code, error_code=error_code)
    else:
        if not app.config["DEBUG"]:
            return ServerError()
        else:
            return e


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], host=app.config["HOST"])




