# -*- coding: utf-8 -*-
# @Time : 2020/5/27 11:47
# @Author : huha
import os,sys,time,copy

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import setting
from proj.tasks import getdomain
from celery.result import AsyncResult
from proj.celery import app

id_dict = {}

# 检查多个队列
def check(id_dict,bool):
    id_dict_c = {}
    while True:
        # 循环检查任务，知道所有任务完成
        for key in id_dict.keys():
            if check_one(key,bool) == 'no done':
                id_dict_c[key] = id_dict[key]
            time.sleep(3)

        if id_dict_c:
            id_dict = copy.copy(id_dict_c)
            id_dict_c = {}

        else:
            print('all done')
            return


# 检测单个队列情况
def check_one(id,bool):
    if bool == 'domain':
        mark = 'domain'
    else:
        mark = 'IP' if bool == 'ip' else 'C scan'
    async_task = AsyncResult(id=id,app=app)
    # 判断异步任务是否执行成功
    if async_task.successful():
        #获取异步任务的返回值
        result = async_task.get()

        if mark != 'C scan':
            print('[-]:{} sub task done({})'.format(mark,id))

        return 'done'
    else:
        if mark != 'C scan':
            print('[-]:{} sub task no done({})'.format(mark, id))
        return 'no done'

# 在备案domain中获取每个域名，每50个域名对应一个任务ID
# 返回任务ID与域名列表相对应的字典
def getsubdomain():
    id_dict = {}
    target_list = []
    thread_num = 50
    count = 0

# 使用线程队列
    with open(setting.ROOT_PATH +'/other/data/备案domain.txt','r',encoding='utf-8') as f:
        target = f.readline().strip('\n')
        # print(target)
        while target:
            target_list.append(target)
            count += 1
            if count == thread_num:
                count = 0
                res = getdomain.delay(target_list)
                id_dict[res.id] = target_list
                target_list = []
            target = f.readline().strip('\n')

        if target_list:
            res = getdomain.delay(target_list)
            id_dict[res.id] = target_list

    return id_dict


if __name__ == '__main__':
    os.system('start cmd /k celery -A proj worker -l info -P eventlet')
    time_start = time.time()
    id_dict = getsubdomain()

    # for key in id_dict.keys():
    #     print(key,id_dict[key])

    # 监控子域名任务
    check(id_dict, 'domain')


    time_end = time.time()
    print('time cost:', "{:.5}".format(time_end - time_start), 'seconds.')