#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os

from flask import Blueprint, request, json, render_template, url_for, flash,redirect


from rss_reader.config import Config
from rss_reader.models import db, RssSource

bp_api = Blueprint(
    __name__,
    __name__,
    static_folder=os.path.join(Config.BASE_DIR, 'static'),
    template_folder=os.path.join(Config.BASE_DIR, 'templates'),
    url_prefix='/api'
)



@bp_api.route('/add', methods=['GET', 'POST'])
def api_add():
    if request.method == 'POST':
        source_url = request.form.get("source_url")
        source_img = request.form.get("source_img")
        source_name = request.form.get("source_name")
        source_sort = request.form.get("source_sort")
        source_tags = request.form.get("source_tags")
        source_desc = request.form.get("source_desc")

        res = RssSource.query.filter_by(source_url=source_url,source_name=source_name).first()

        if res == None:
            data = RssSource(source_url=source_url,
                             source_img=source_img,
                             source_name=source_name,
                             source_sort=source_sort,
                             source_tags=source_tags,
                             source_desc=source_desc,)
            db.session.add(data)
            db.session.commit()
            return('恭喜您，添加源成功！')
        else:
            return('您添加的源已经存在！')



@bp_api.route('/delete/<source_id>', methods=['GET', 'POST'])
def api_delete(source_id):
    if source_id:

        res = RssSource.query.filter_by(source_id=source_id).first()

        if res != None:
            db.session.delete(res)
            db.session.commit()
            return ('恭喜您，源已成功删除！')
        else:
            return ('抱歉，此源不存在，无法删除！')


@bp_api.route('/alter/<source_id>', methods=['GET', 'POST'])
def api_alter(source_id):
    if request.method == 'POST':
        source_url = request.form.get("source_url")
        source_img = request.form.get("source_img")
        source_name = request.form.get("source_name")
        source_sort = request.form.get("source_sort")
        source_tags = request.form.get("source_tags")
        source_desc = request.form.get("source_desc")

        res = RssSource.query.filter_by(source_id=source_id).first()

        if res != None:
            res.source_url = source_url
            res.source_img = source_img
            res.source_name = source_name
            res.source_sort = source_sort
            res.source_tags = source_tags
            res.source_desc = source_desc
            db.session.commit()
        else:
            return ("抱歉，此源不存在！")



@bp_api.route('/search', methods=['GET', 'POST'])
def api_search():
    if request.method == 'POST':
        source_url_name = request.form.get("source_url_name")

        res = RssSource.query.filter_by(source_name=source_url_name).first()
        sources = []

        if res != None:
            sources.append({'id': res.source_id,
                            'img': res.source_img,
                            'name': res.source_name,
                            'sort': res.source_sort,
                            'tags': res.source_tags,
                            'desc': res.source_desc, })
            return render_template('rss_search.html', sources=sources)

        else:
            return ('抱歉，此源不存在！')

