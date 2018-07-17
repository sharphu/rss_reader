#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os


from flask import Blueprint, request, url_for,redirect
from flask import render_template
from sqlalchemy import or_

from rss_reader.config import Config
from rss_reader.models import db,RssSource

bp_traf = Blueprint(
    __name__,
    __name__,
    static_folder=os.path.join(Config.BASE_DIR, 'static'),
    template_folder=os.path.join(Config.BASE_DIR, 'templates'),
    url_prefix='/traf'
)



@bp_traf.route('/add', methods=['GET', 'POST'])
def add_source():
    return render_template('rss_add_alter.html',handle_name='add')



@bp_traf.route('/alter/<source_id>', methods=['GET','POST'])
def alter_source(source_id):
    return render_template('rss_add_alter.html',handle_name='alter',source_id=source_id)


@bp_traf.route('/search/<tags_sort>')
def search_source(tags_sort):
    if tags_sort:
        res = RssSource.query.filter(or_(RssSource.source_sort==tags_sort,
                                         RssSource.source_tags==tags_sort)).all()

        sources = []

        if res != None:
            for rs in res:
                sources.append({'id': rs.source_id,
                                'img': rs.source_img,
                                'name': rs.source_name,
                                'sort': rs.source_sort,
                                'tags': rs.source_tags,
                                'desc': rs.source_desc, })
            return render_template('rss_search.html', sources=sources)

        else:
            return render_template('feedback.html',img_name = 'Not_found.jpg')
            # return ('抱歉，此源不存在！')

