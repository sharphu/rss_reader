import os

from flask import Flask

from rss_reader.config import Config
from rss_reader.models import db, RssSource

sources = [{
    'url': 'http://feed.cnblogs.com/blog/u/118754/rss',
    'img': '1.jpg',
    'name': 'Vamei',
    'tag': 'Python',
    'desc': '编程，数学，设计'
}, {
    'url': 'http://www.dongwm.com/atom.xml',
    'img': '2.jpg',
    'name': '小明明之美',
    'tag': 'Python',
    'desc': '一个Python手艺',
}, {
    'url': 'https://coolshell.cn/feed',
    'img': '3.jpg',
    'name': '酷壳',
    'tag':'Article',
    'desc': 'Coding Your Ambition',
}, {
    'url': 'http://www.alibuybuy.com/feed',
    'img': '4.jpg',
    'name': '互联网的那点事',
    'tag':'Article',
    'desc': '聚焦互联网前沿资讯！',
}, {
    'url': 'http://www.geekpark.net/rss',
    'img': '5.jpg',
    'name': '极客公园',
    'tag': 'Digital',
    'desc': '极客公园',
}, {
    'url': 'http://36kr.com/feed',
    'img': '6.jpg',
    'name': '36氪',
    'tag': 'Innovation',
    'desc': '36氪 - 让创业更简单。'
}, {
    'url': 'http://www.apprcn.com/feed',
    'img': '7.jpg',
    'name': '反斗软件',
    'tag':'Article',
    'desc': '关注个人软件和绿色软件。',
}, {
    'url': 'https://feed.iplaysoft.com/',
    'img': '8.jpg',
    'name': '异次元软件世界',
    'tag':'Downloads',
    'desc': '软件改变生活！',
}, {
    'url': 'https://www.cnbeta.com/backend.php',
    'img': '9.jpg',
    'name': 'cnBeta',
    'tag':'News',
    'desc': '简明IT新闻,网友媒体与言论平台！',
}, {
    'url': 'http://www.diy-robots.com/?feed=rss2',
    'img': '10.jpg',
    'name': '做做AI，造造人',
    'tag':'Blog',
    'desc': '动手改变世界。',
}, {
    'url': 'http://blog.zhaojie.me/rss',
    'img': '11.jpg',
    'name': '老赵点滴',
    'tag':'Blog',
    'desc': '追求编程之美。',
}, {
    'url': 'http://feed.mifengtd.cn/',
    'img': '12.jpg',
    'name': '褪墨',
    'tag':'Blog',
    'desc': '我们的目标是：把事情做到更好！',
}, {
    'url': 'http://news.feng.com/rss.xml',
    'img': '13.jpg',
    'name': '威锋网',
    'tag':'iPhone',
    'desc': 'iPhone讨论社区！',
}, {
    'url': 'http://www.uisdc.com/feed',
    'img': '14.jpg',
    'name': '优设-UISDC',
    'tag':'Article',
    'desc': '设计师交流学习平台。',
}, {
    'url': 'http://www.ifanr.com/feed',
    'img': '15.jpg',
    'name': '爱范儿',
    'tag':'Consumption',
    'desc': '让未来触手可及！',
},{
    'url': 'http://cinephilia.net/feed',
    'img': '16.jpg',
    'name': 'cinephilia迷影',
    'tag': 'Moves',
    'desc': '认真说好每一个故事',
}, {
    'url': 'http://www.phonekr.com/feed/',
    'img': '17.jpg',
    'name': '锋客网',
    'tag': 'Phone',
    'desc': 'techXtreme 科技锋芒',
}, {
    'url': 'http://pansci.asia/feed',
    'img': '18.jpg',
    'name': 'PanSci 泛科學',
    'tag':'Article',
    'desc': '全台最大科學知識社群。',
},]

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
                             source_tag=source['tag'],
                             source_desc=source['desc'],
                             )
            db.session.add(data)
            db.session.commit()
