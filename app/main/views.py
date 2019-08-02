#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 下午9:12
# @Author  : Chilson
# @Email   : qiushun_fang@126.com

from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm
from .. import db
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    # 如果提交表单,向session塞数据,重新渲染页面
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            user = User(username=form.username.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['username'] = form.name.data
        form.name.data = ''
        return redirect(url_for('main.index'))
    return render_template('index.html', form=form, username=session.get(
        'username'), known=session.get('known', False))
