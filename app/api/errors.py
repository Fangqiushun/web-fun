#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2019/8/18 上午9:24
# @Author  : Chilson
# @Email   : qiushun_fang@126.com

from flask import request, jsonify
from . import api
from wtforms.validators import ValidationError


def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response


def unauthorized(message):
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.status_code = 401
    return response


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response


@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])
