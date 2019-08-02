#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 下午7:08
# @Author  : Chilson
# @Email   : qiushun_fang@126.com

import os
# 当前文件路径的绝对路径
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """通用配置类"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'My girl friend is Natalie!'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.126.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '25'))
    MAIL_USE_TLS = os.environ.get(
        'MAIL_USE_TLS', 'true').lower() in [
        'true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASK_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASK_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASK_ADMIN = os.environ.get('FLASK_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    """测试环境配置"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TEST_DATABASE_URL') or 'sqlite://'


class ProductionConfig(Config):
    """生产环境配置"""
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'PRO_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

if __name__ == '__main__':
    print(Config.__dict__)