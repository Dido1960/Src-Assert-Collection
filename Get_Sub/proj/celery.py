#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc:
author: huha
'''
# absolute_import 保证从绝对路径引入celery，防止导入时目录下celery.py文件覆盖celery库文件
from __future__ import absolute_import
from celery import Celery


app = Celery('proj',
             broker='redis://127.0.0.1',
             backend='redis://127.0.0.1',
             include=['proj.tasks'])


if __name__=='__main__':
    app.start()