#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os

from flask import Blueprint, render_template, json
from rss_reader.config import Config
from rss_reader.models import db, RssSource

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
        return render_template('404.html')
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




    # 'dongwm': 'http://www.dongwm.com/atom.xml',
    # 'cnblogs': 'http://feed.cnblogs.com/blog/u/118754/rss',
    # 'cinephilia': 'http://cinephilia.net/feed',
    # 'phonekr': 'http://www.phonekr.com/feed/',
    # 'geekpark': 'http://www.geekpark.net/rss',
    # '36kr': 'http://36kr.com/feed',
    # 'asia': 'http://pansci.asia/feed',
    # 'ifanr': 'http://www.ifanr.com/feed',
    # 'apprcn': 'http://www.apprcn.com/feed',
    # 'alibuybuy': 'http://www.alibuybuy.com/feed',
    # 'iplaysoft': 'https://feed.iplaysoft.com/',
    # 'uisdc': 'http://www.uisdc.com/feed',
    # 'coolshell': 'https://coolshell.cn/feed',
    # 'mifengtd': 'http://feed.mifengtd.cn/',
    # 'robots': 'http://www.diy-robots.com/?feed=rss2',
    # 'zhaojie': 'http://blog.zhaojie.me/rss',
    # 'cnbeta': 'https://www.cnbeta.com/backend.php',
    # 'feng': 'http://news.feng.com/rss.xml',

    # sources2 = [{
    #     'url': '/rss/asia',
    #     'img': '7.jpg',
    #     'title': 'PanSci 泛科學'
    # }, {
    #     'url': '/rss/ifanr',
    #     'img': '8.jpg',
    #     'title': '爱范儿'
    # }, {
    #     'url': '/rss/apprcn',
    #     'img': '9.jpg',
    #     'title': '反斗软件'
    # }, {
    #     'url': '/rss/alibuybuy',
    #     'img': '10.jpg',
    #     'title': '互联网的那点事'
    # }, {
    #     'url': '/rss/iplaysoft',
    #     'img': '11.jpg',
    #     'title': '异次元软件世界'
    # }, {
    #     'url': '/rss/uisdc',
    #     'img': '12.jpg',
    #     'title': '优设-UISDC'
    # }]
    #
    # sources3 = [{
    #     'url': '/rss/coolshell',
    #     'img': '13.jpg',
    #     'title': '酷壳'
    # }, {
    #     'url': '/rss/mifengtd',
    #     'img': '14.jpg',
    #     'title': '褪墨・时间管理'
    # }, {
    #     'url': '/rss/robots',
    #     'img': '15.jpg',
    #     'title': '做做AI，造造人'
    # }, {
    #     'url': '/rss/zhaojie',
    #     'img': '16.jpg',
    #     'title': '老赵点滴・追求编程之美'
    # }, {
    #     'url': '/rss/cnbeta',
    #     'img': '17.jpg',
    #     'title': 'cnBeta・简明IT新闻'
    # }, {
    #     'url': '/rss/feng',
    #     'img': '18.jpg',
    #     'title': '威锋网'
    # }]
    return render_template('home.html', sources=sources, pages=pages)
