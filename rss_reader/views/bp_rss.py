#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os

from flask import Blueprint
from flask import render_template

from rss_reader.config import Config
from rss_reader.models import RssSource
from rss_reader.database.redis import base_cache

bp_rss = Blueprint(
    __name__,
    __name__,
    static_folder=os.path.join(Config.BASE_DIR, 'static'),
    template_folder=os.path.join(Config.BASE_DIR, 'templates'),
    url_prefix='/rss'
)


@bp_rss.route('/<source_id>', methods=['GET'])
def index(source_id):
    res = RssSource.query.filter_by(source_id=int(source_id)).first()
    if res:

        key = res.source_url

        result = base_cache.parse_cache(url=key, dynamic_key=key)

        return render_template('rss_detail.html', data=result[key])
    else:
        return render_template('feedback.html', img_name='Not_found.jpg')