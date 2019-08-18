#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2019/8/18 上午9:21
# @Author  : Chilson
# @Email   : qiushun_fang@126.com

from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, comments, errors, posts, users
