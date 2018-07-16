#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class RssSource(db.Model):
    __tablename__ = 'rss_source'
    source_id = db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
    source_url = db.Column(db.String(100),nullable=False)
    source_img = db.Column(db.String(100),nullable=False)
    source_name = db.Column(db.String(20),nullable=False)
    source_sort = db.Column(db.String(20),nullable=False)
    source_tags = db.Column(db.String(20),nullable=False)
    source_desc = db.Column(db.String(100),nullable=False)


    def __init__(self,source_url,source_img,source_name,source_sort,source_tags,source_desc):
        self.source_url = source_url
        self.source_img = source_img
        self.source_name = source_name
        self.source_sort = source_sort
        self.source_tags = source_tags
        self.source_desc = source_desc

    def __repr__(self):
        return '<RssSource %r>' % self.__class__.__name__
