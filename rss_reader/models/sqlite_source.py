import os

from flask import Flask

from rss_reader.config import Config
from rss_reader.models import db, RssSource

sources = [{
    'url': 'http://www.dongwm.com/atom.xml',
    'img': '1.jpg',
    'name': '小明明之美',
    # 'sort': '编程',
    'tags': 'Python',
    'desc': '一个Python手艺',
}, {
    'url': 'http://feed.cnblogs.com/blog/u/118754/rss',
    'img': '2.jpg',
    'name': 'Vamei',
    # 'sort': '编程',
    'tags': 'Python',
    'desc': '编程，数学，设计'
}, {
    'url': 'http://cinephilia.net/feed',
    'img': '3.jpg',
    'name': 'cinephilia迷影',
    # 'sort': '影视',
    'tags': 'Moves',
    'desc': '认真说好每一个故事',
}, {
    'url': 'http://www.phonekr.com/feed/',
    'img': '4.jpg',
    'name': '锋客网',
    # 'sort': '科技',
    'tags': 'Phone',
    'desc': 'techXtreme 科技锋芒',
}, {
    'url': 'http://www.geekpark.net/rss',
    'img': '5.jpg',
    'name': '极客公园',
    # 'sort': '科技',
    'tags': 'Digital',
    'desc': '极客公园',
}, {
    'url': 'http://36kr.com/feed',
    'img': '6.jpg',
    'name': '36氪',
    # 'sort': '创业',
    'tags': 'Innovation',
    'desc': '36氪 - 让创业更简单。'
}, {
    'url': 'http://pansci.asia/feed',
    'img': '7.jpg',
    'name': 'PanSci 泛科學',
    # 'sort': '科学',
    'tags':'Article',
    'desc': '全台最大科學知識社群。',
}, {
    'url': 'http://www.ifanr.com/feed',
    'img': '8.jpg',
    'name': '爱范儿',
    # 'sort': '时尚',
    'tags':'Consumption',
    'desc': '让未来触手可及！',
}, {
    'url': 'http://www.apprcn.com/feed',
    'img': '9.jpg',
    'name': '反斗软件',
    # 'sort': '软件',
    'tags':'Article',
    'desc': '关注个人软件和绿色软件。',
}, {
    'url': 'http://www.alibuybuy.com/feed',
    'img': '10.jpg',
    'name': '互联网的那点事',
    # 'sort': '互联网',
    'tags':'Article',
    'desc': '聚焦互联网前沿资讯！',
}, {
    'url': 'https://feed.iplaysoft.com/',
    'img': '11.jpg',
    'name': '异次元软件世界',
    # 'sort': '软件',
    'tags':'Downloads',
    'desc': '软件改变生活！',
}, {
    'url': 'http://www.uisdc.com/feed',
    'img': '12.jpg',
    'name': '优设-UISDC',
    # 'sort': '设计',
    'tags':'Article',
    'desc': '设计师交流学习平台。',
}, {
    'url': 'https://coolshell.cn/feed',
    'img': '13.jpg',
    'name': '酷壳',
    # 'sort': '编程',
    'tags':'Article',
    'desc': 'Coding Your Ambition',
}, {
    'url': 'http://feed.mifengtd.cn/',
    'img': '14.jpg',
    'name': '褪墨',
    # 'sort': '管理',
    'tags':'Blog',
    'desc': '我们的目标是：把事情做到更好！',
}, {
    'url': 'http://www.diy-robots.com/?feed=rss2',
    'img': '15.jpg',
    'name': '做做AI，造造人',
    # 'sort': '科技',
    'tags':'Blog',
    'desc': '动手改变世界。',
}, {
    'url': 'http://blog.zhaojie.me/rss',
    'img': '16.jpg',
    'name': '老赵点滴',
    # 'sort': '编程',
    'tags':'Blog',
    'desc': '追求编程之美。',
}, {
    'url': 'https://www.cnbeta.com/backend.php',
    'img': '17.jpg',
    'name': 'cnBeta',
    # 'sort': '新闻',
    'tags':'News',
    'desc': '简明IT新闻,网友媒体与言论平台！',
}, {
    'url': 'http://news.feng.com/rss.xml',
    'img': '18.jpg',
    'name': '威锋网',
    # 'sort': '新闻',
    'tags':'iPhone',
    'desc': 'iPhone讨论社区！',
}]

app = Flask(__name__)

if __name__ == '__main__':
    db_path = os.path.join(Config.BASE_DIR, 'models/rss_reader.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    db.init_app(app)
    db.create_all(app=app)
    with app.app_context():
        for source in sources:
            data = RssSource(source_url=source['url'],
                             source_img=source['img'],
                             source_name=source['name'],
                             source_tags=source['tags'],
                             source_desc=source['desc'],
                             )
            db.session.add(data)
            db.session.commit()
