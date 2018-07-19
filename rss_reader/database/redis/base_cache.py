from feedparser import parse

from expire import cached,CacheSetting

from rss_reader.database.redis import MySettings

@cached(**MySettings.cache, ttl=1000)
def parse_cache(url,params=None,**kwargs):
    feed = parse(url)
    articles = feed['entries']
    data = []
    for article in articles:
        data.append({"title": article["title_detail"]["value"],
                     "link": article["link"],
                     "published": article["published"].split('T', 1)[0] or article["published"].split('+', 1)[0],
                     })

    return {url:data}


def cached_by_redis(key):
    cache_ins = CacheSetting(MySettings)
    return cache_ins.get(key)

