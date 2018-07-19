#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os

from flask import Blueprint, render_template
from rss_reader.config import Config
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
    if nums == 1:
        pages = [1, 2]
    else:
        pages = [nums - 1, nums + 1]

    start = (nums - 1) * 6 + 1
    stop = nums * 6
    sources = []

    res_start = RssSource.query.filter_by(source_id=start).first()
    res_stop = RssSource.query.filter_by(source_id=stop).first()
    if res_start == None:
        return render_template('feedback.html',img_name = '404.jpg')
    elif res_stop == None:
        while (1):
            res = RssSource.query.filter_by(source_id=start).first()
            if res != None:
                start += 1
                sources.append({'id': res.source_id,
                                'img': res.source_img,
                                'name': res.source_name,
                                'tags': res.source_tags,
                                'desc': res.source_desc,})
            else:
                break
        return render_template('home.html', sources=sources, pages=pages)
    else:
        for i in range(start, stop + 1):
            res = RssSource.query.filter_by(source_id=i).first()
            sources.append({'id': res.source_id,
                            'img': res.source_img,
                            'name': res.source_name,
                            'tags': res.source_tags,
                            'desc': res.source_desc, })
        return render_template('home.html', sources=sources, pages=pages)
