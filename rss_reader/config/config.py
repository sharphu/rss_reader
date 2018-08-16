#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os


class Config:
    DEBUG = os.environ.get('DEBUG', False)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    RSS_DICT = {
        'dongwm': 'http://www.dongwm.com/atom.xml',
        'cnblogs': 'http://feed.cnblogs.com/blog/u/118754/rss',
        'cinephilia': 'http://cinephilia.net/feed',
        'phonekr': 'http://www.phonekr.com/feed/',
        'geekpark': 'http://www.geekpark.net/rss',
        '36kr': 'http://36kr.com/feed',
        'asia': 'http://pansci.asia/feed',
        'ifanr': 'http://www.ifanr.com/feed',
        'apprcn': 'http://www.apprcn.com/feed',
        'alibuybuy': 'http://www.alibuybuy.com/feed',
        'iplaysoft': 'https://feed.iplaysoft.com/',
        'uisdc': 'http://www.uisdc.com/feed',
        'coolshell': 'https://coolshell.cn/feed',
        'mifengtd': 'http://feed.mifengtd.cn/',
        'robots': 'http://www.diy-robots.com/?feed=rss2',
        'zhaojie': 'http://blog.zhaojie.me/rss',
        'cnbeta': 'https://www.cnbeta.com/backend.php',
        'feng': 'http://news.feng.com/rss.xml',

    }
