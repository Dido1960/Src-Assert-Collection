# -*- coding: utf-8 -*-
# @Time : 2020/5/27 11:47
# @Author : huha
# 从页面正则匹配出src列表
import re
import os.path
import glob
import setting
from core import util


class parse:
    def __init__(self,path):
        self.path = path

    # 设置正则匹配模板，从rule.txt读取规则
    def setpattern(self,num):
        # print(config.ROOT_PATH.replace("\\","/")+ '/data/rule.txt')
        with open(setting.ROOT_PATH + '/other/data/rule.txt','r',encoding='utf-8') as f:
            rule = f.read()
            # print(rule)
        pattern = re.findall(num+'\.html\n(.*?)\n(.*?)\n',rule)
        # print(pattern)
        return pattern

    # 解析页面
    def parse_one_page(self):
        with open(self.path,'r',encoding='utf-8') as f:
            self.html = f.read()
        pattern1 = re.compile(self.pattern[0][0], re.S)
        pattern2 = re.compile(self.pattern[0][1], re.S)
        content = re.findall(pattern1, self.html)[0]
        items = re.findall(pattern2, content)
        return items

    def run(self, path):
        num = os.path.basename(self.path)[0]
        self.pattern = self.setpattern(num)
        # print(self.pattern)
        if os.path.exists(path):
            os.remove(path)
        items = self.parse_one_page()
        for x in range(len(items)):
           with open(path,'a+',encoding='utf-8') as f:
               if items[x][-1]== '/':
                   items[x] = items[x][:-1]
               f.write(items[x]+'\n')
           print(items[x])

if __name__ == '__main__':
    # setting.a()
    # print(setting.ROOT_PATH)
    # 循环爬取多个页面1.html 2.html 3.html
    for name in glob.glob(setting.ROOT_PATH + '/other/data/*'):
        if 'html' in name:
            p = parse(name)
            p.run(setting.ROOT_PATH + '/other/data/src.txt')

    # 去重去空行
    util.out_file(setting.ROOT_PATH + "/other/data/src.txt")