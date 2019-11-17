#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc:
author: huha
'''
import re
import os
from selenium import webdriver
import requests
import re
from IPy import IP
import threading
import time
import urllib3
urllib3.disable_warnings()

# 正则匹配获取一级域名
def get_one_level_domain(path):
    key_list = []
    with open (path,'r',encoding='utf-8') as f:
        url = f.readline()
        while url:
            url_match = re.findall(r'(\w*)\.(.*-?\w*)\.(\w*)\.?(\w*)', url)
        # print(url_match)
            if url_match:
                key = url_match[0][1]+'.'+url_match[0][2]
                key_list.append(key)
            url = f.readline()
    return key_list

# 去重去空行
def out_file(path):
    file_list = []  # 创建一个空列表
    with open(path, "r", encoding="utf-8") as f:
        file_2 = f.readlines()
    for file in file_2:
        file_list.append(file)
    out_file1 = set(file_list)    #set()函数可以自动过滤掉重复元素
    last_out_file = list(out_file1)
    os.remove(path)
    for out in last_out_file:
        with open(path,"a+",encoding="utf-8") as f:   #去重后文件写入文件里
            if out != '\n':
                f.write(out)

# 模拟浏览器获取页面元素
def getajaxpage(url):
    browser = webdriver.PhantomJS()
    # browser.get('https://security.alibaba.com/global.htm?spm=0.0.0.0.jbZNqu')
    browser.get(url)
    html = browser.page_source
    browser.close()
    return html

def cscan_one(ip,ip_all):
    domains = set()
    # if '://' in ip:
    # print(ip)
    # ip = ip.split('://')[-1].split(':')[0]
    q = "https://www.bing.com/search?q=ip:" + str(ip)
    # print(q)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}

    r = requests.get(q, headers=headers, verify=False,proxies=proxies)
    c = r.content.decode()
    p = re.compile(r'<cite>(.*?)</cite>')
    l = re.findall(p, c)
    for each in l:
        domain = each.split('://')[-1].split('/')[0]
        domains.add(domain)

    if not domains:
        # print(str(ip)+' False')
        return False
    else:
        print(str(ip)+' True')
        ip_all.append(ip)
        return True


def cscan(CIDR):
    ip_all = []
    # CIDR = '139.129.132.0/29'
    print('[-]:扫'+CIDR+' C段')
    ip_list = []
    for ip in IP(CIDR):
        ip_list.append(ip)

    threads = []
    for ip in ip_list:
        threads.append(threading.Thread(target=cscan_one,args=(ip,ip_all),daemon=True))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return ip_all
    # return 1



# def getTitle(input):
#     """
#     Get title from html-content/ip/url
#
#     :param input:html-content OR ip OR url
#     :return text in <title>
#     :except return string:'NULL'
#     """
#     try:
#         if '<title>' in input:
#             content = input
#         else:
#             url = 'http://' + input if '://' not in input else input
#             # print(url)
#             r = requests.get(input, timeout=3,
#                          headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'})
#             return re.findall(b'<title>([\s\S]*)</title>', r.content)[0].strip()
#
#     except Exception:
#         return ''

if __name__ == '__main__':
   cscan_one('139.129.132.6',[])