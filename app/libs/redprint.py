# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2018/12/15 17:17


# 红图类 注册路由
class Redprint(object):
    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))
            return f
        return decorator

    def register(self, blue_print, url_prefix=None):
        if url_prefix is None:
            url_prefix = "/" + self.name
        for f, rule, options in self.mound:
            endpoint = self.name + "+" + options.pop("endpoint", f.__name__)
            # print(endpoint) url_for()时传入使用
            blue_print.add_url_rule(url_prefix + rule, endpoint, f, **options)

