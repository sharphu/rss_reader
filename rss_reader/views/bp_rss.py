#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os


from feedparser import parse
from flask import Blueprint, request, url_for, json
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

        key = res.source_id
        value = data


        result = redisbase.parse_cache(url=key, dynamic_key=key, params=value)
        # return render_template('rss_detail.html', data=result['1'])
        print(result)
        print(redisbase.cached_by_redis(key))
        return json.dumps(result)

        # return render_template('rss_detail.html', data=redisbase.cached_by_redis(key))
        # return redisbase.cached_by_redis(key)



        # if redisbase.cached_by_redis(key):
        #     result = redisbase.cached_by_redis(key)
        # else:
        #     result = redisbase.parse_cache(url=key, dynamic_key=key, params=value)
        # print(result)
        # print(redisbase.cached_by_redis(key))
        #
        # return render_template('rss_detail.html', data=result)

        # result = redisbase.parse_cache(url=key, value=value)
        # print(result)
        # print(redisbase.cached_by_redis(key))

        # key = 'expire'
        # value = {
        #     '234': 'tatatat',
        #     '1234': 'huhuhu'
        # }
        #
        # # set
        # result = redisbase.parse_cache(url=key, dynamic_key = key, params=value)
        # print(result)

        # get
        # print(redisbase.cached_by_redis(key))

    else:
        return 'source_id is null'








