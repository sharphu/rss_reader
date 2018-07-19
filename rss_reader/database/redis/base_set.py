#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from expire import Settings
from expire import RedisCache,JsonSerializer


class MySettings(Settings):
    cache = {
        'cache_class':RedisCache,
        'cache_config':{
            'host': '127.0.0.1',
            'port': 6379,
            'db': 0,
            'password': None
        },
        'serializer': JsonSerializer
    }
