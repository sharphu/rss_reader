#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os

from flask import Blueprint, request, render_template
from sqlalchemy import or_


from rss_reader.config import Config
from rss_reader.models import db, RssSource

bp_api = Blueprint(
    __name__,
    __name__,
    static_folder=os.path.join(Config.BASE_DIR, 'static'),
    template_folder=os.path.join(Config.BASE_DIR, 'templates'),
    url_prefix='/api'
)



@bp_api.route('/add/<id_img>', methods=['GET', 'POST'])
def api_add(id_img):
    if request.method == 'POST':
        source_url = request.form.get("source_url")
        source_name = request.form.get("source_name")
        source_tags = request.form.get("source_tags")
        source_desc = request.form.get("source_desc")

        res = RssSource.query.filter_by(source_url=source_url,source_name=source_name).first()

        if res == None:
            data = RssSource(source_url=source_url,
                             source_img=str(id_img)+'.jpg',
                             source_name=source_name,
                             source_tags=source_tags,
                             source_desc=source_desc,)
            db.session.add(data)
            db.session.commit()
            return render_template('feedback.html', img_name='success.jpg',back_text='恭喜您，添加源成功！')
        else:
            return render_template('feedback.html', img_name='existed.jpg',back_text='抱歉，您添加的源已经存在！')



@bp_api.route('/delete/<source_id>', methods=['GET', 'POST'])
def api_delete(source_id):
    if source_id:

        res = RssSource.query.filter_by(source_id=source_id).first()

        if res != None:
            db.session.delete(res)
            db.session.commit()
            return render_template('feedback.html', img_name='success.jpg', back_text='恭喜您，源已成功删除！')
        else:
            return render_template('feedback.html', img_name = 'Not_found.jpg')
            # return ('抱歉，此源不存在，无法删除！')


@bp_api.route('/alter/<id_img>', methods=['GET', 'POST'])
def api_alter(id_img):
    if request.method == 'POST':
        source_url = request.form.get("source_url")
        source_name = request.form.get("source_name")
        source_tags = request.form.get("source_tags")
        source_desc = request.form.get("source_desc")

        res = RssSource.query.filter_by(source_id=id_img).first()

        if res != None:
            res.source_url = source_url
            res.source_img = res.source_img
            res.source_name = source_name
            res.source_tags = source_tags
            res.source_desc = source_desc
            db.session.commit()
            return render_template('feedback.html', img_name='success.jpg',back_text='恭喜您，修改源成功！')
        else:
            return render_template('feedback.html',img_name = 'Not_found.jpg')
            # return ("抱歉，此源不存在！")



@bp_api.route('/search', methods=['GET', 'POST'])
def api_search():
    if request.method == 'POST':
        source_url_name = request.form.get("source_url_name")

        res = RssSource.query.filter(or_(RssSource.source_name==source_url_name,
                                         RssSource.source_tags==source_url_name)).all()

        sources = []

        if len(res) != 0:
            for rs in res:
                sources.append({'id': rs.source_id,
                                'img': rs.source_img,
                                'name': rs.source_name,
                                'tags': rs.source_tags,
                                'desc': rs.source_desc, })
            return render_template('rss_search.html', sources=sources)
        else:
            return render_template('feedback.html',img_name = 'Not_found.jpg')
            # return ('抱歉，此源不存在！')

