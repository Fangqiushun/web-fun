#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 下午7:07
# @Author  : Chilson
# @Email   : qiushun_fang@126.com

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
