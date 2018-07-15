#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os

from pprint import pprint

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


# @bp_rss.route('/<rss_name>', methods=['GET'])
# def index(rss_name):
#     url = Config.RSS_DICT.get(rss_name)
#     if url:
#         feed = parse(url)
#         pprint(feed)
#         articles = feed['entries']
#         data = []
#         for article in articles:
#             data.append({"title": article["title_detail"]["value"],
#                          "link": article["link"],
#                          "published": article["published"].split('T',1)[0] or article["published"].split('+',1)[0],
#                          })
#     else:
#         data = {'info': 'rss_name is null'}
#     return render_template('rss_name.html', title=rss_name, data=data)



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
    return render_template('rss_name.html', data=data)



@bp_rss.route('/sou/<handle_source>', methods=['GET', 'POST'])
def add_source(handle_source):
    if handle_source == 'add_source':
        content_dict = {'handle_name': handle_source, 'source_url': 'http://127.0.0.1:5000/api/add'}
        return render_template('rss_source.html', content_dict=content_dict)
    elif handle_source == 'delete_source':
        content_dict = {'handle_name': handle_source, 'source_url': 'http://127.0.0.1:5000/api/delete'}
        return render_template('rss_search_source.html', content_dict=content_dict)
    elif handle_source == 'alter_source':
        content_dict = {'handle_name': handle_source, 'source_url': 'http://127.0.0.1:5000/api/alter_source'}
        return render_template('rss_search_source.html', content_dict=content_dict)
    else:
        content_dict = {'handle_name': handle_source, 'source_url': 'http://127.0.0.1:5000/api/search'}
        return render_template('rss_search_source.html', content_dict=content_dict)

# @bp_rss.route('/add_source',methods=['GET','POST'])
# def add_source():
#     return render_template('rss_source.html')
#
# @bp_rss.route('/delete_source',methods=['GET','POST'])
# def add_source():
#     return render_template('rss_source.html')
#
# @bp_rss.route('/alter_source',methods=['GET','POST'])
# def add_source():
#     return render_template('rss_source.html')
