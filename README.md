web-fun
===========================
一个基于flask的博客（《FlaskWeb开发基于python的web应用开发实战》实现）

## 功能介绍
* 账户管理
* 写博客
* 关注用户
* 评论博客

## 版本
* 系统: ubuntu64位
* python: 3.6.7

## 目录结构
    ├── app                 -- 应用目录
    │   ├── auth            -- 用户接口
    │   │   ├── forms.py    -- 用户表单
    │   │   ├── __init__.py -- 初始化脚本
    │   │   └── views.py    -- 用户视图
    │   ├── email.py        -- 邮件模块
    │   ├── __init__.py     --初始化脚本
    │   ├── main            -- 主应用
    │   │   ├── errors.py   -- 错误视图
    │   │   ├── forms.py    -- 表单
    │   │   ├── __init__.py -- 初始化脚本
    │   │   └── views.py    -- 视图
    │   ├── models.py       -- 数据结构
    │   ├── static          -- 静态文件
    │   └── templates       -- 模板
    ├── config.py           -- 配置文件
    ├── data-dev.sqlite     -- 开发环境数据库（启动开发环境的时候才会有）
    ├── data.sqlite         -- 线上环境数据库（启动线上环境的时候才会有）
    ├── Pipfile             -- 依赖
    ├── Pipfile.lock        -- 依赖
    ├── README.md           -- 说明文档
    ├── tests               -- 测试
    └── web_fun.py          -- 应用入口


## 安装
```bash
pip install pipenv
pipenv install 
```

## 启动
```bash
export FLASK_ENV=development       # <testing|development|production>
export FLASK_APP=web_fun.py
export MAIL_PASSWORD=****
# 初始化数据库
flask db init
flask db migrate
flask db upgrade
# 启动应用
flask run
```

