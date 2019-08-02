#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2019/7/30 下午11:16
# @Author  : Chilson
# @Email   : qiushun_fang@126.com

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
