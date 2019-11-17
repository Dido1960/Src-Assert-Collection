#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc:
author: huha
'''
from proj.tasks import getdomain, getip, cscan
from celery.result import AsyncResult
from proj.celery import app
import time
import copy
import glob
import core.util as util

id_dict = {}
# 检查多个队列
def check(id_dict,bool):
    id_dict_c = {}
    id_dict_ip = {}
    # print(type(id_dict))
    while True:
        for key in id_dict.keys():
            # print(key)
            if check_one(key,bool) == 'no done':
                id_dict_c[key] = id_dict[key]
            elif bool == 'domain':
                # print(id_dict[key])
                res = getip.delay(id_dict[key])
                id_dict_ip[res.id] = id_dict[key]
                # print('-'*10)
                # print(res.id)
                # print('-'*10)
            time.sleep(3)
        if id_dict_c:
            id_dict = copy.copy(id_dict_c)
            id_dict_c = {}
        else:
            if id_dict_ip:
                return id_dict_ip
            else:
                return 'all done'

# 检测单个队列情况
def check_one(id,bool):
    if bool == 'domain':
        mark = '子域名'
    else:
        mark = 'IP' if bool == 'ip' else 'C段扫描'
    async_task = AsyncResult(id=id,app=app)
    # 判断异步任务是否执行成功
    if async_task.successful():
        #获取异步任务的返回值
        result = async_task.get()
        print(id)
        print(mark+'子任务已经执行完成')
        return 'done'
    else:
        print(id)
        print(mark+"子任务还未执行完成")
        return 'no done'

def getsubdomain():
    id_dict = {}
    target_list = []
    thread_num = 10
    count = 0
    with open('D:/2.auxiliary means/2-30python/FsrcAssets/data/maindomain.txt','r',encoding='utf-8') as f:
        target = f.readline().strip('\n')
        # print(target)
        while target:
            target_list.append(target)
            count += 1
            if count == thread_num:
                res = getdomain.delay(target_list)
                id_dict[res.id] = target_list
                count = 0
                target_list = []
            target = f.readline().strip('\n')

        if target_list:
            res = getdomain.delay(target_list)
            id_dict[res.id] = target_list

    return id_dict

# 多线程队列
if __name__ == '__main__':
    id_dict = getsubdomain()
    # for key in id_dict.keys():
    #     print(key,id_dict[key])
    # 监视获取子域名队列
    id_dict_ip = check(id_dict,'domain')
    # 监视获取IP队列
    print(check(id_dict, 'ip'))