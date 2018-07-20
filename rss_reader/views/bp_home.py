#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os

from flask import Blueprint, render_template

from rss_reader.config import Config
from rss_reader.database.redis import base_cache
from rss_reader.models import RssSource

bp_home = Blueprint(
    __name__,
    __name__,
    static_folder=os.path.join(Config.BASE_DIR, 'static'),
    template_folder=os.path.join(Config.BASE_DIR, 'templates'),
    url_prefix='/'
)


@bp_home.route('/page/<int:nums>', methods=['GET'])
@bp_home.route('/', methods=['GET'])
def index(nums=1):
    if nums < 1:
        nums = 1
    result_data = RssSource.query.offset((nums - 1) * 6).limit(6).all()
    sources = []
    for each in result_data:
        sources.append({
            "source_id": each.source_id,
            "source_url": each.source_url,
            "source_img": each.source_img,
            "source_name": each.source_name,
            "source_tags": each.source_tags,
            "source_desc": each.source_desc,
        })
    return render_template('home.html', sources=sources, pages=nums)


@bp_home.route('/rss/<source_id>', methods=['GET'])
def rss(source_id):
    res = RssSource.query.filter_by(source_id=int(source_id)).first()
    if res:
        key = res.source_url
        result = base_cache.parse_cache(url=key, dynamic_key=key)
        return render_template('rss_source_detail.html', data=result[key])
    else:
        return render_template('feedback.html', img_name='Not_found.jpg')


@bp_home.route('/rss/source', methods=['GET'])
def rss_source():
    result_data = RssSource.query.all()
    sources = []
    for each in result_data:
        sources.append({
            "source_id": each.source_id,
            "source_url": each.source_url,
            "source_img": each.source_img,
            "source_name": each.source_name,
            "source_tags": each.source_tags,
            "source_desc": each.source_desc,
        })
    return render_template('rss_source_manage.html', sources=sources)

@bp_home.route('/rss/tag', methods=['GET'])
def rss_tag():
    result_data = RssSource.query.all()
    sources = []
    for each in result_data:
        sources.append(each.source_tags)
    return render_template('rss_tag_manage.html', sources=list(set(sources)))