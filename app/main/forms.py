#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 下午9:12
# @Author  : Chilson
# @Email   : qiushun_fang@126.com

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    """名字表单"""
    username = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField('Submit')