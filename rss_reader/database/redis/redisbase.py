#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from expire import Settings
from expire import RedisCache,cached,CacheSetting


class MySettings(Settings):
    cache = {
        'cache_class':RedisCache,
        'cache_config':{
            'host': '127.0.0.1',
            'port': 6379,
            'db': 0,
            'password': None
        },
        'serializer': None
    }

@cached(**MySettings.cache, ttl=50)
def parse_cache(url,params=None,**kwargs):
    data={
        '123':'hahah',
        '1234':'huhuhu'
    }
    return "{0}:{1}".format(url,params)


def cached_by_redis(key):
    cache_ins = CacheSetting(MySettings)
    return cache_ins.get(key)


if __name__ == '__main__':
    key = 'keep'

    #set
    result = parse_cache(url = key, dynamic_key = key)
    print(result)

    #get
    print(cached_by_redis(key))