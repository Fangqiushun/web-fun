#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2019/8/4 下午11:03
# @Author  : Chilson
# @Email   : qiushun_fang@126.com

import logging
import functools

x = 10


def use_logging(level='info'):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if level == 'warning':
                logging.warning("%s is running" % func.__name__)
            elif level == 'info':
                logging.info("%s is running" % func.__name__)
            else:
                logging.error("%s is running" % func.__name__)
            return func(*args, **kwargs)

        return wrapper
    return decorator


@use_logging()
def foo():
    global x
    x += 1
    print(x)


if __name__ == '__main__':
    print(foo())
