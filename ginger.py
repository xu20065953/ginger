# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2018/12/15 16:54

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], host=app.config["HOST"])




