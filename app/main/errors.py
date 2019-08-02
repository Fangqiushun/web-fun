#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 下午9:12
# @Author  : Chilson
# @Email   : qiushun_fang@126.com

from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
