#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os


from feedparser import parse
from flask import Blueprint, request, url_for
from flask import render_template
from expire import Settings
from expire import RedisCache,cached,CacheSetting

from rss_reader.config import Config
from rss_reader.models import db, RssSource

import sys
sys.path.append('/home/wind/Documents/Programming/Python/Project/rss_reader/rss_reader/database/redis')
import redisbase

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
        re_data = {res.source_name:data}
        # key = res.source_name
        # value = data
        # # if redisbase.cached_by_redis(key):
        # #     result = redisbase.cached_by_redis(key)
        # # else:
        # #     result = redisbase.parse_cache(url=key,value=value)
        # # print(result)
        #
        # result = redisbase.parse_cache(url=key, value=value)
        # print(result)
        # print(redisbase.cached_by_redis(key))

        key = 'expire'

        # set
        result = redisbase.parse_cache(url=key, dynamic_key=key)
        print(result)

        # get
        print(redisbase.cached_by_redis(key))

    else:
        result = {'info': 'source_id is null'}
    return render_template('rss_detail.html', data=result)







