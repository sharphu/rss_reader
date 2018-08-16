#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
import random

from flask import Blueprint, request, render_template, json
from sqlalchemy import or_

from rss_reader.config import Config
from rss_reader.models import db, RssSource

bp_api = Blueprint(
    __name__,
    __name__,
    static_folder=os.path.join(Config.BASE_DIR, 'static'),
    template_folder=os.path.join(Config.BASE_DIR, 'templates'),
    url_prefix='/api'
)


@bp_api.route('/add', methods=['GET', 'POST'])
def api_add():
    try:
        data = request.get_json()
        print(data)
        print(request.json)
        source_url = data['source_url']
        source_img = random.randint(1,29)
        source_name = data['source_name']
        source_tag = data['source_tag']
        source_desc = data['source_desc']
        res = RssSource.query.filter_by(source_url=source_url,source_name=source_name).first()

        if res == None:
            add_data = RssSource(source_url=source_url,
                             source_img=str(source_img) + '.jpg',
                             source_name=source_name,
                             source_tag=source_tag,
                             source_desc=source_desc, )
            db.session.add(add_data)
            db.session.commit()
            return json.dumps({'status': 1})
        else:
            return json.dumps({'status': 0})
    except Exception as e:
        print(e)
        return json.dumps({'status': 0})


    # if request.method == 'POST':
    #     source_url = request.form.get("source_url")
    #     source_img = random.randint(1, 29)
    #     source_name = request.form.get("source_name")
    #     source_tag = request.form.get("source_tag")
    #     source_desc = request.form.get("source_desc")
    #
    #     res = RssSource.query.filter_by(source_url=source_url, source_name=source_name).first()
    #
    #     if res == None:
    #         data = RssSource(source_url=source_url,
    #                          source_img=str(source_img) + '.jpg',
    #                          source_name=source_name,
    #                          source_tag=source_tag,
    #                          source_desc=source_desc, )
    #         db.session.add(data)
    #         db.session.commit()
    #         return json.dumps({'status': 1})
    #     else:
    #         return json.dumps({'status': 0})


@bp_api.route('/delete/<source_id>', methods=['GET'])
def api_delete(source_id):
    try:
        if source_id:
            res = RssSource.query.filter_by(source_id=int(source_id)).first()
            db.session.delete(res)
            db.session.commit()
            return json.dumps({'status': 1})
        else:
            return json.dumps({'status': 1})
    except Exception as e:
        print(e)
        return json.dumps({'status': 1})


@bp_api.route('/update', methods=['POST'])
def api_alter():
    try:
        data = request.get_json()
        print(data)
        print(request.json)
        source_id = data['source_id']
        source_url = data['source_url']
        source_name = data['source_name']
        source_tag = data['source_tag']
        source_desc = data['source_desc']
        res = RssSource.query.filter_by(source_id=source_id).first()

        if res != None:
            res.source_url = source_url
            res.source_img = res.source_img
            res.source_name = source_name
            res.source_tag = source_tag
            res.source_desc = source_desc
            db.session.commit()
            return json.dumps({'status': 1})
        else:
            return json.dumps({'status': 0})
    except Exception as e:
        print(e)
        return json.dumps({'status': 0})


@bp_api.route('/search', methods=['GET', 'POST'])
def api_search():
    source_tag = str(request.args.get('wd', '')).strip()
    if request.method == 'POST':
        source_tag = request.form.get("source_tag")
    else:
        source_tag = source_tag
    res = RssSource.query.filter(RssSource.source_tag == source_tag).all()

    # res = RssSource.query.filter(or_(RssSource.source_name == source_tag,
    #                                  RssSource.source_tag == source_tag)).all()

    sources = []

    if len(res) != 0:
        for rs in res:
            sources.append({'source_id': rs.source_id,
                            'source_img': rs.source_img,
                            'source_name': rs.source_name,
                            'source_tag': rs.source_tag,
                            'source_desc': rs.source_desc, })
        return render_template('rss_source_manage.html',sources=sources)
        # return json.dumps({'status': 1})
    else:
        return json.dumps({'status': 0})
