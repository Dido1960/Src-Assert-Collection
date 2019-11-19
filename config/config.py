#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc:
author: huha
'''
import os
import json

ROOT_PATH = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])
with open(ROOT_PATH.replace("\\", "/") + '/data/txt/ua.json', 'r', encoding='utf8') as f:
    UA = json.loads(f.read())
# print(ROOT_PATH)