#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os

from flask import Blueprint, render_template

from rss_reader.config import Config
from rss_reader.models import RssSource
from rss_reader.database.redis import base_cache

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
    source_data = found_source()

    quotient = len(source_data)//6
    remainder = len(source_data)%6

    if nums == 1:
        pages = [1, 2]
    else:
        pages = [nums - 1, nums + 1]

    if nums <= quotient:
        start = (nums - 1) * 6
        stop = nums * 6 - 1
        sources = []

        for i in range(start, stop + 1):
            res = source_data[i]
            sources.append({'id': res["id"],
                            'img': res["img"],
                            'name': res["name"],
                            'tags': res["tags"],
                            'desc': res["desc"], })
        return render_template('home.html', sources=sources, pages=pages)
    else:
        if remainder == 0:
            return render_template('feedback.html', img_name='404.jpg')
        else:
            surplus = source_data[(nums-1)*6:]
            if surplus != []:
                sources = []
                for res in surplus:
                    sources.append({'id': res["id"],
                                    'img': res["img"],
                                    'name': res["name"],
                                    'tags': res["tags"],
                                    'desc': res["desc"], })
                return render_template('home.html', sources=sources, pages=pages)
            else:
                return render_template('feedback.html', img_name='404.jpg')

def found_source():
        num = 1
        count = 0
        count2 = 0
        source_data = []
        while (1):
            res = RssSource.query.filter_by(source_id=num).first()
            if res:
                if count2 != 6:
                    source_data.append({'id': res.source_id,
                                        'img': res.source_img,
                                        'name': res.source_name,
                                        'tags': res.source_tags,
                                        'desc': res.source_desc, })
                    num += 1
                else:
                    break
            else:
                if count != 6:
                    count += 1
                    num += 1
                else:
                    break
        return source_data





