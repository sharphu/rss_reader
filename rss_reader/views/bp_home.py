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





    # start = (nums - 1) * 6 + 1
    # stop = nums * 6
    # sources = []
    #
    # num = start
    # count = 0
    # count2 = 0
    # source_data = []
    # while (1):
    #     res = RssSource.query.filter_by(source_id=num).first()
    #     if res:
    #         if count2 != 6:
    #             source_data.append({'id': res.source_id,
    #                                 'img': res.source_img,
    #                                 'name': res.source_name,
    #                                 'tags': res.source_tags,
    #                                 'desc': res.source_desc, })
    #             count2 += 1
    #             num += 1
    #         else:
    #             break
    #     else:
    #         if count != 4:
    #
    #             count += 1
    #             num += 1
    #         else:
    #             return render_template('feedback.html', img_name='404.jpg')
    # return source_data






    # key = 'data'
    # result = base_cache.home_cache(url=key, dynamic_key=key)
    # source_data = result[key]
    # print(base_cache.cached_by_redis(key))
    # if nums == 1:
    #     pages = [1, 2]
    # else:
    #     pages = [nums - 1, nums + 1]
    #
    #
    # start = (nums - 1) * 6
    # stop = nums * 6 - 1
    # sources = []
    #
    # res_start = source_data[start]
    # res_stop = source_data[stop]

    # try:
    #     print(source_data[start])
    #     try:
    #         print(source_data[stop])
    #     except:
    #
    # except:
    #     return render_template('feedback.html', img_name='404.jpg')

    # if res_start == None:
    #     return render_template('feedback.html', img_name='404.jpg')
    # elif res_stop == None:
    #     while (1):
    #         res = source_data[start]
    #         if res != None:
    #             start += 1
    #             sources.append({'id': res["id"],
    #                             'img': res["img"],
    #                             'name': res["name"],
    #                             'tags': res["tags"],
    #                             'desc': res["desc"], })
    #         else:
    #             break
    #     return render_template('home.html', sources=sources, pages=pages)
    # else:
    #     for i in range(start, stop + 1):
    #         res = source_data[i]
    #         sources.append({'id': res["id"],
    #                         'img': res["img"],
    #                         'name': res["name"],
    #                         'tags': res["tags"],
    #                         'desc': res["desc"], })
    #     return render_template('home.html', sources=sources, pages=pages)

'''
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

'''


