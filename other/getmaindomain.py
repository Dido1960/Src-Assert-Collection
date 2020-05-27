# -*- coding: utf-8 -*- 
# @Time : 2020/5/27 11:47
# @Author : huha
import requests
import re
from core import util
import setting
import os


def getbeian():
    key_list = util.get_one_level_domain(setting.ROOT_PATH + '/other/data/src.txt')
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
            # print(match)
    # print(beian_list)
    domain_list1 = []
    ip_list = []
    for x in range(len(beian_list)):
        # print(beian_list[x].split(" "))
        domain_list1 += beian_list[x].split(" ")
    domain_list2 = domain_list1[:]

    # 去除IP
    for x in range(len(domain_list1)):
        match = re.findall('^[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}$',domain_list1[x])
        if match:
            domain_list2.remove(match[0])
            # ip_list += match

    # for x in range(len(ip_list)):
    #     path = setting.ROOT_PATH + '/data/备案ip.txt'
    #     with open(setting.ROOT_PATH + '/data/备案ip.txt', 'a+') as f:
    #         f.write(ip_list[x]+'\n')

    # 写进文件
    path = setting.ROOT_PATH + '/other/data/备案domain.txt'
    if os.path.exists(path):
        os.remove(path)
    for y in range(len(domain_list2)):
        with open(path, 'a+',encoding = 'utf-8') as f:
            f.write(domain_list2[y] + '\n')
    return domain_list2

def run():
    # 通过站长备案查询域名备案信息，写进文件
    getbeian()
    # print(a)

    # 处理备案文件格式
    domain = util.get_one_level_domain(setting.ROOT_PATH + '/other/data/备案domain.txt')
    path = setting.ROOT_PATH + '/other/data/备案domain.txt'
    if os.path.exists(path):
        os.remove(path)
    with open(path,'a+',encoding='utf-8') as f:
        for x in range(len(domain)):
            f.write(domain[x]+'\n')

if __name__ == '__main__':
    run()