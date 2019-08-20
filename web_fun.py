#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 下午7:08
# @Author  : Chilson
# @Email   : qiushun_fang@126.com

import os
from flask_migrate import upgrade
from app.models import Role, User

COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()

from flask_migrate import Migrate
from app.models import User, Role
from app import create_app, db
import click
import sys
from logging import Logger

logger = Logger('Web-Fun')


app = create_app(os.getenv('FLASK_ENV') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


@app.cli.command()
@click.option('--coverage/--no-coverage', default=False, help='Run tests under code coverage.')
@click.argument('test_names', nargs=-1)
def test(coverage, test_names):
    """跑单元测试"""
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        import subprocess
        os.environ['FLASK_COVERAGE'] = '1'
        logger.warning(sys.argv)
        sys.exit(subprocess.call(sys.argv))

    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()


@app.cli.command()
@click.option('--length', default=25, help='Number of functions to include in the profiler report.')
@click.option('--profile-dir', default=None, help='Directory where profiler data files are saved.')
def profile(length, profile_dir):
    """在代码分析器上启动应用"""
    from werkzeug.middleware.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length], profile_dir=profile_dir)
    app.run(debug=False)


@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # 把数据库迁移到最新修订版本
    upgrade()

    # 创建或更新用户角色
    Role.insert_roles()

    # 确保所有用户都关注了他们自己
    User.add_self_follows()