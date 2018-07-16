#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os


from feedparser import parse
from flask import Blueprint, request, url_for
from flask import render_template

from rss_reader.config import Config
from rss_reader.models import db, RssSource

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
        feed = parse(res.source_url)
        articles = feed['entries']
        data = []
        for article in articles:
            data.append({"title": article["title_detail"]["value"],
                         "link": article["link"],
                         "published": article["published"].split('T', 1)[0] or article["published"].split('+', 1)[0],
                         })
    else:
        data = {'info': 'source_id is null'}
    return render_template('rss_detail.html', data=data)








