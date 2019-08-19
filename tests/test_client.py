#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2019/8/18 下午8:12
# @Author  : Chilson
# @Email   : qiushun_fang@126.com

import unittest
import re
from app import create_app, db
from app.models import User, Role
from logging import Logger

logger = Logger('test')

class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Role.insert_roles()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Stranger' in response.get_data(as_text=True))

    def test_register_and_login(self):
        # 注册新账户
        response = self.client.post('/auth/register', data={
            'email': 'chilson@example.com',
            'username': 'chilson',
            'password': 'handsome',
            'password2': 'handsome'
        })
        self.assertEqual(response.status_code, 302)

        # 使用新注册的帐号登录
        response = self.client.post('/auth/login', data={
            'email': 'chilson@example.com',
            'password': 'handsome'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # logger.error(response.get_data(as_text=True))
        self.assertTrue(re.search('您好,\s+Chilson', response.get_data(as_text=True)))
        self.assertTrue('你还没有确认注册哦!' in response.get_data(as_text=True))

        # 发送确认令牌
        user = User.query.filter_by(email='chilson@example.com').first()
        token = user.generate_confirmation_token()
        response = self.client.get('/auth/confirm/{}'.format(token), follow_redirects=True)
        user.confirm(token)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('You have confirmed your account' in response.get_data(as_text=True))

        # 退出
        response = self.client.get('/auth/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('You have been logged out' in response.get_data(as_text=True))