#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc:
author: huha
'''
import requests
import re
from core import util


def getbeian():
    key_list = util.get_one_level_domain('./data/src.txt')
    # print(key_list)
    # key = 'tuniu.com'
    beian_list = []
    for x in range(len(key_list)):
    # for x in range(2):
    #站长备案查询
        api = 'http://icp.chinaz.com/ajaxsync.aspx?at=beiansl&callback=jQuery111301768215955620236_1573664260451&host={0}&type=host&_=1573664260452'.format(key_list[x])
        # api = 'http://icp.chinaz.com/ajaxsync.aspx?at=beiansl&callback=jQuery111301768215955620236_1573664260451&host=qunar.com&type=host&_=1573664260452'
        print(api)
        r = requests.get(api)
        # r.encoding = 'utf-8'
        text = r.text
        # print(text)
        pattern = re.compile('MainPage:"(.*?)"', re.S)
        match = re.findall(pattern, text)
        if match:
            beian_list += match
            # with open('./data/beian.txt','w+') as f:
            #     f.write()
            print(match)
    # print(beian_list)
    domain_list1 = []
    ip_list = []
    for x in range(len(beian_list)):
        # print(beian_list[x].split(" "))
        domain_list1 += beian_list[x].split(" ")
    domain_list2 = domain_list1[:]
    for x in range(len(domain_list1)):
        match = re.findall('^[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}$',domain_list1[x])
        if match:
            domain_list2.remove(match[0])
            ip_list += match

    for x in range(len(ip_list)):
        with open('./data/备案ip.txt', 'a+') as f:
            f.write(ip_list[x]+'\n')

    for y in range(len(domain_list2)):
        with open('./data/备案domain.txt', 'a+') as f:
            f.write(domain_list2[y]+'\n')

    print(ip_list)
    print(domain_list2)

if __name__ == '__main__':
    # 利用备案反查获取域名
    # getbeian()

    # 整理出maindomain
    maindomain = util.get_one_level_domain('./data/备案domain.txt')
    with open('./data/maindomain.txt','w+',encoding='utf-8') as f:
        for x in range(len(maindomain)):
            f.write(maindomain[x]+'\n')