from feedparser import parse

from expire import cached, CacheSetting

from rss_reader.database.redis import MySettings
from rss_reader.models import RssSource


@cached(**MySettings.cache, ttl=1000)
def parse_cache(url, params=None, **kwargs):
    feed = parse(url)
    articles = feed['entries']
    data = []
    for article in articles:
        data.append({"title": article["title_detail"]["value"],
                     "link": article["link"],
                     "published": article["published"].split('T', 1)[0] or article["published"].split('+', 1)[0],
                     })

    return {url: data}


# @cached(**MySettings.cache, ttl=10)
# def home_cache(url, params=None, **kwargs):
#     sources = found_source()
#     return {url: sources}
#
#
# def found_source():
#     num = 1
#     count = 0
#     count2 = 0
#     source_data = []
#     while (1):
#         res = RssSource.query.filter_by(source_id=num).first()
#         if res:
#             if count2 != 6:
#                 source_data.append({'id': res.source_id,
#                                     'img': res.source_img,
#                                     'name': res.source_name,
#                                     'tags': res.source_tags,
#                                     'desc': res.source_desc, })
#                 num += 1
#             else:
#                 break
#         else:
#             if count != 6:
#                 count += 1
#                 num += 1
#             else:
#                 break
#     return source_data


def cached_by_redis(key):
    cache_ins = CacheSetting(MySettings)
    return cache_ins.get(key)
