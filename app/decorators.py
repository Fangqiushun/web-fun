#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 下午11:09
# @Author  : Chilson
# @Email   : qiushun_fang@126.com

from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission


def permission_required(permission):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return func(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(func):
    return permission_required(Permission.ADMIN)(func)