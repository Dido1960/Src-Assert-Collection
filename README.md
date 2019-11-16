## Src-Assert-Collection
* 子域名收集与C段扫描，利用Celery+Redis实现分布式队列，方便任务管理
* 收集IP资产，用于POC批量测试国内各大Src业务
* enumerate subdomains of websites using OSINT，使用[Sublist3r](https://github.com/aboul3la/Sublist3r)项目API收集子域名
* 基于Bing搜索引擎扫描C段

## Requirement
* 本地安装celery
* 需要将core,Sublist3r包路径导入PYTHONPATH
* windows下进入GetSub目录  
  celery -A proj worker -l info -P eventlet  
  启动worker


## data目录
* data/src.txt  
各大Src域名(/core/getsrc.py爬取)

* data/maindomain.txt  
基于站长备案查询(/core/getmaindomain.py)  

* data/subdomainip  
基于OSINT枚举子域名，dns解析各域名A记录

* data/ip.txt  
Bing引擎C段扫描整理最后的IP资产


  
