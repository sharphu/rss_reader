#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os

from flask import Blueprint, request, json, render_template, url_for, flash,redirect
from sqlalchemy import or_
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from rss_reader.config import Config
from rss_reader.models import db, RssSource

bp_api = Blueprint(
    __name__,
    __name__,
    static_folder=os.path.join(Config.BASE_DIR, 'static'),
    template_folder=os.path.join(Config.BASE_DIR, 'templates'),
    url_prefix='/api'
)


# class SourceForm(Form):
#     source_url = StringField('url:',validators=[DataRequired()])
#     source_img = StringField('img:',validators=[DataRequired()])
#     source_name = StringField('name:',validators=[DataRequired()])
#     submit = SubmitField('提交')

@bp_api.route('/add', methods=['GET', 'POST'])
def api_add():
    # source_form = SourceForm()
    if request.method == 'POST':
        source_url = request.form.get("source_url")
        source_img = request.form.get("source_img")
        source_name = request.form.get("source_name")
        source_tags = request.form.get("source_tags")

        '''
            p1 = request.form.get("userName")
            res = {'status': p1}
            return json.dumps(res)
        '''
        res = RssSource.query.filter_by(source_url=source_url).first()

        if res == None:
            data = RssSource(source_url=source_url, source_img=source_img, source_name=source_name,source_tags=source_tags)
            db.session.add(data)
            db.session.commit()
            return('恭喜您，添加源成功！')
        else:
            return('您添加的源已经存在！')
    # return render_template('rss_source.html')

    '''
        try:
        data = RssSource(source_url=source_url, source_img=source_img, source_name=source_name)
        db.session.add(data)
        db.session.commit()
        res = {'status': 1, 'info': 'ok'}
        except:
        res = {'status': -1, 'info': 'failed'}
        return json.dumps(res)
    '''



@bp_api.route('/delete', methods=['GET', 'POST'])
def api_delete():
    if request.method == 'POST':
        source_url_name = request.form.get("source_url_name")

        res = RssSource.query.filter_by(source_name=source_url_name).first()

        if res != None:
            db.session.delete(res)
            db.session.commit()
            return ('恭喜您，源已成功删除！')
        else:
            return ('抱歉，此源不存在，无法删除！')

@bp_api.route('/alter_source', methods=['GET','POST'])
def api_alter_source():
    if request.method == 'POST':
        source_url_name = request.form.get("source_url_name")

        res = RssSource.query.filter_by(source_name=source_url_name).first()


        # res = RssSource.query.filter_by(or_(
        #     source_id=source_url_name,
        #     source_url=source_url_name,
        #     source_name=source_url_name,
        # )
        # ).all()



        if res != None:
            return render_template('rss_alter_source.html', source_alter_id=res.source_id)
        else:
            return ('抱歉，此源不存在！')

@bp_api.route('/alter/<source_alter_id>', methods=['GET', 'POST'])
def api_alter(source_alter_id):
    if request.method == 'POST':
        # source_id = request.form.get("source_id")
        source_url = request.form.get("source_url")
        source_img = request.form.get("source_img")
        source_name = request.form.get("source_name")
        source_tags = request.form.get("source_tags")
    res = RssSource.query.filter_by(source_id=source_alter_id).first()

    if res != None:
        res.source_url = source_url
        res.source_img = source_img
        res.source_name = source_name
        res.source_tags = source_tags
        db.session.commit()
        return ('恭喜您，源已成功修改！')
    # elif res2 != None:
    #     res2.source_url = source_url
    #     res2.source_img = source_img
    #     res2.source_name = source_name
    #     db.session.commit()
    #     return ('恭喜您，源已成功修改！')
    # elif res3 != None:
    #     res3.source_url = source_url
    #     res3.source_img = source_img
    #     res3.source_name = source_name
    #     db.session.commit()
    #     return ('恭喜您，源已成功修改！')
    else:
        return ('抱歉，此源不存在，无法修改！')


    # if res == None:
    #     return 'This is None'
    # else:
    #     old_source_url = res.source_url
    #     old_source_img = res.source_img
    #     old_source_name = res.source_name
    #     res.source_url = '123'
    #     res.source_img = '244'
    #     res.source_name = '234'
    #     db.session.commit()


@bp_api.route('/search', methods=['GET', 'POST'])
def api_search():
    if request.method == 'POST':
        source_url_name = request.form.get("source_url_name")

        # print(db.session.query(RssSource).filter(or_(RssSource.source_id == source_url_name, RssSource.source_name == source_url_name)).all())

        # res = db.session.query(RssSource).filter(
        #     RssSource.source_id == int(source_url_name),
        #     # RssSource.source_id == source_url_name,
        #     # RssSource.source_name == source_url_name
        # ).all()
        # res = RssSource.query.filter(RssSource.source_id ==int(source_url_name)).first()

        res = RssSource.query.filter_by(source_name=source_url_name).first()

        if res != None:
            # print(res.source_id)
            rss_url1 = 'http://127.0.0.1:5000/rss/' + str(res.source_id)
            # print('数据id是：' + str(res.source_id))
            # print('source应用图片：' + res.source_img)
            return redirect(rss_url1)
            # return ('123')
        else:
            return ('抱歉，此源不存在！')


        # res1 = RssSource.query.filter_by(source_id=source_url_name).first()
        # res2 = RssSource.query.filter_by(source_url=source_url_name).first()
        # res3 = RssSource.query.filter_by(source_name=source_url_name).first()
        #
        # if res1 != None:
        #     rss_url1 = 'http://127.0.0.1:5000/rss/' + str(res1.source_id)
        #     print('数据id是：' + str(res1.source_id))
        #     print('source应用图片：' + res1.source_img)
        #     return redirect(rss_url1)
        # elif res2 != None:
        #     rss_url2 = 'http://127.0.0.1:5000/rss/' + str(res2.source_id)
        #     print('数据id是：' + str(res2.source_id))
        #     print('source应用图片：' + res2.source_img)
        #     return redirect(rss_url2)
        # elif res3 != None:
        #     rss_url3 = 'http://127.0.0.1:5000/rss/' + str(res3.source_id)
        #     print('数据id是：' + str(res3.source_id))
        #     print('source应用图片：'+res3.source_img)
        #     return  redirect(rss_url3)
        #     # return redirect(url_for('http://127.0.0.1:5000/rss/'.join(str(res2.source_id))))
        #     # print('数据id是：'+str(res2.source_id))
        #     # return ('恭喜您，源已查到！')
        # else:
        #     return ('抱歉，此源不存在！')

    # print(res.source_url, res.source_img, res.source_name)
    # return '22'
