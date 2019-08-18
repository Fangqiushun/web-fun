#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2019/8/18 上午9:24
# @Author  : Chilson
# @Email   : qiushun_fang@126.com

from functools import wraps
from flask import g
from .errors import forbidden

def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbidden('Insufficient permissions')
            return f(*args, **kwargs)
        return decorated_function
    return decorator
