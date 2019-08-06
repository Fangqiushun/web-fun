web-fun
===========================
一个基于flask的web后台

## 功能介绍
1. 账户管理
2. 商品查询(启动爬虫脚本) [todo] 
3. 单平台商品比价排名/销售量排名/评价排名 [todo] 
4. 多平台总体数据排名(商品均价/总销量/评价均值) [todo] 
5. 指定算法,自动推荐 [todo]
6. 选取多算法,准确率比较 [todo] 

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
    │   │   └── shit.ico
    │   └── templates       -- 模板
    │       ├── 404.html
    │       ├── 500.html
    │       ├── auth
    │       │   ├── email
    │       │   │   └── confirm.txt
    │       │   ├── login.html
    │       │   ├── register.html
    │       │   └── unconfirmed.html
    │       ├── base.html
    │       ├── hello.html
    │       └── index.html
    ├── config.py           -- 配置文件
    ├── data-dev.sqlite     -- 开发环境数据库
    ├── data.sqlite         -- 线上环境数据库
    ├── Pipfile             -- 依赖
    ├── Pipfile.lock        -- 依赖
    ├── README.md           -- 说明文档
    ├── tests               -- 测试
    │   ├── __init__.py
    │   ├── test_basics.py
    │   └── test_user_models.py
    └── web-fun.py          -- 应用入口


## 安装
```bash
pip install pipenv
pipenv install 
```

## 启动
```bash
export FLASK_ENV=development       # <testing|development|production>
export FLASK_APP=web-fun.py
export MAIL_PASSWORD=****
flask run
```

