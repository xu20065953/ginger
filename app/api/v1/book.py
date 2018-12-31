# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2018/12/15 16:59
from flask import request, jsonify
from sqlalchemy import or_

from app.libs.redprint import Redprint
from app.models.book import Book

api = Redprint("book")


@api.route("/search", methods=["POST"])
def book_search():
    q = request.json.get('q', '')
    q = "%" + q + "%"
    book = Book.query.filter(or_(Book.title.like(q), Book.publisher.like(q))).all()
    return jsonify(book)


