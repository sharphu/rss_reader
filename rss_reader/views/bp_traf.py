#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os


from flask import Blueprint, request, url_for
from flask import render_template

from rss_reader.config import Config

bp_traf = Blueprint(
    __name__,
    __name__,
    static_folder=os.path.join(Config.BASE_DIR, 'static'),
    template_folder=os.path.join(Config.BASE_DIR, 'templates'),
    url_prefix='/traf'
)



@bp_traf.route('/add', methods=['GET', 'POST'])
def add_source():
    return render_template('rss_add_alter.html',handle_name='add')



@bp_traf.route('/alter/<source_id>', methods=['GET','POST'])
def alter_source(source_id):
    return render_template('rss_add_alter.html',handle_name='alter',source_id=source_id)