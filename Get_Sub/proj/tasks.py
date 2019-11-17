#/usr/bin/python
#coding:utf-8

from __future__ import absolute_import
from Sublist3r import sublist3r
from proj.celery import app
import threading
import dns.resolver
import time
import os
import core.util as util
import queue

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

@app.task(time_limit=1)
def getdomain(target_list):
    start = time.time()
    # baidu,bing,netcraft,dnsdumpster,ssl
    # virustotal,threatcrowd,passivedns
    threads = []
    for target in target_list:
        print(target)
        threads.append(threading.Thread(target=sublist3r.main,
                                        args=(target, 40, 'D:/2.auxiliary means/2-30python/FsrcAssets/data/subdomain/'+target+'.txt'),
                                        kwargs={'ports':None, 'silent':False, 'verbose': True, 'enable_bruteforce':False, 'engines':'passivedns,ssl,threatcrowd,netcraft'}))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return 1

@app.task
def getip(domain_list):
    ip_list = []
    domain = ''
    subdomain_list = []
    for domain in domain_list:
        path = '../data/subdomain/' + domain + '.txt'
        if os.path.exists(path):
            print('-' * 10)
            with open(path,'r',encoding='utf-8') as f:
                while domain:
                    subdomain_list.append(domain)
                    domain = f.readline().strip('\n')
            # print(subdomain_list)
            for domain in subdomain_list:
                print(domain)
                try:
                    record = dns.resolver.query(domain)
                    for A_CNAME in record.response.answer:
                        for item in A_CNAME.items:
                            if item.rdtype == dns.rdatatype.from_text('A'):
                                ip_list.append(str(item))
                                # print(str(item))
                except:
                    pass

                if ip_list:
                    ip_path = '../data/subdomainip/' + domain + '_ip.txt'
                    print(ip_path)
                    print(ip_list)
                    with open(ip_path, 'w+', encoding='utf-8') as f:
                        for x in range(len(ip_list)):
                            f.write(ip_list[x] + '\n')
                # util.out_file(ip_path)
                ip_list = []
            print('-'*10)
    # with open('../../data/full.txt','a',encoding='utf-8') as f:
    #     for x in range(len(ip_list)):
    #         f.write(ip_list[x]+'\n')
    return 1


@app.task
def cscan(CIDR_list):
    print('-'*20)
    # print(CIDR_list)
    for CIDR in CIDR_list:
        ip_list = util.cscan(CIDR)
        # print('../data/ip/'+CIDR.split("/")[0]+'.txt')
        with open('D:/2.auxiliary means/2-30python/FsrcAssets/data/ip/'+CIDR.split("/")[0]+'.txt','a',encoding='utf-8') as f:
            for ip in ip_list:
                # print(ip)
                f.write(str(ip)+'\n')
    print('-'*10)
    return 1