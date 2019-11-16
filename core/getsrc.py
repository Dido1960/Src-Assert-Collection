#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc:
author: huha
'''
import re
import os.path
import glob


class parse:
    def __init__(self,path):
        self.path = path

    def setpattern(self,num):
        with open('D:/2.auxiliary means/2-30python/CTF/src/data/rule.txt','r',encoding='utf-8') as f:
            rule = f.read()
        pattern = re.findall(num+'\.html\n(.*?)\n(.*?)\n',rule)
        # print(pattern)
        return pattern

    def parse_one_page(self):
        with open(self.path,'r',encoding='utf-8') as f:
            self.html = f.read()
        pattern1 = re.compile(self.pattern[0][0], re.S)
        pattern2 = re.compile(self.pattern[0][1], re.S)
        content = re.findall(pattern1, self.html)[0]
        items = re.findall(pattern2, content)
        return items

    def run(self):
        num = os.path.basename(self.path)[0]
        self.pattern = self.setpattern(num)
        # print(self.pattern)
        items = self.parse_one_page()
        for x in range(len(items)):
           with open('./data/src.txt','w+',encoding='utf-8') as f:
               if items[x][-1]== '/':
                   items[x] = items[x][:-1]
               f.write(items[x]+'\n')
           print(items[x])

if __name__ == '__main__':
    # 正则匹配各大src
    for name in glob.glob('./data/*'):
        if 'html' in name:
            p = parse(name)
            p.run()
    # 去重去空行
    # util.out_file("./data/src.txt")