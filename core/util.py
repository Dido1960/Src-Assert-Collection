# -*- coding: utf-8 -*-
# @Time : 2020/5/27 11:47
# @Author : huha
import os,re,urllib3
from selenium import webdriver
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
