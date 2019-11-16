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
import start

def scan():
    cscan_dict = {}
    CIDR_all = []
    thread_num = 10
    count = 0
    ip_list = []
    for name in glob.glob('../data/subdomainip/*'):
        with open(name,'r',encoding='utf-8') as f:
            ip = f.readline().strip('\n')
            while ip:
                ip_list.append(ip)
                CIDR = ".".join(ip.split(".")[:-1]) + '.0/24'
                if CIDR not in CIDR_all and CIDR.split(".")[0] != '127':
                    CIDR_all.append(CIDR)
                    count += 1
                    if count == thread_num:
                        res = cscan.delay(CIDR_all)
                        cscan_dict[res.id] = CIDR_all
                        count = 0
                        CIDR_all = []
                ip = f.readline().strip('\n')
        with open('../data/ip.txt','w',encoding='utf-8') as f:
            for ip in ip_list:
                f.write(ip+'\n')
    if CIDR_all:
        res = cscan.delay(CIDR_all)
        cscan_dict[res.id] = CIDR_all

    return cscan_dict

if __name__ == '__main__':
    cscan_dict = scan()
    # print(cscan_dict)
    print(start.check(cscan_dict,'cscan'))