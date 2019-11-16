#/usr/bin/python
#coding:utf-8

from __future__ import absolute_import
from celery import Celery
import sys
# absolute_import 保证从绝对路径引入celery，防止倒入时目录下celery.py文件覆盖celery库文件

sys.path.append('D:/2.auxiliary means/2-30python/FsrcAssets/core')
app = Celery('proj', broker='redis://localhost',
        backend='redis://localhost', include=['proj.tasks'])
#将proj目录下tasks加进来

app.config_from_object('proj.config')
#使用config.py作为配置文件，也可以直接在这里写相关配置信息

if __name__=='__main__':
    app.start()