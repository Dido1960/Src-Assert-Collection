
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
  
* /Get_Sub/start.py发布子域名收集任务并监控
* /Get_Sub/cscan_check.py发布C段扫描收集任务并监控


## data目录
* data/src.txt  
各大Src域名(/core/getsrc.py爬取)

* data/maindomain.txt  
基于站长备案查询(/core/getmaindomain.py)  

* data/subdomainip  
基于OSINT枚举子域名，dns解析各域名A记录

* data/ip  
Bing引擎C段扫描整理最后的IP资产

## Screenshots
收集子域名并实时监控 

![标题](https://img-blog.csdnimg.cn/20191117130239263.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODA5ODk2,size_16,color_FFFFFF,t_70)

收集C段IP并实时监控 

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191117130443689.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODA5ODk2,size_16,color_FFFFFF,t_70)

使用burp代理绕过ssl证书检测，默认使用8080端口  

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191117131612473.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODA5ODk2,size_16,color_FFFFFF,t_70)


## TODO
* 文件路径修改
* 配置参数模块化
* /data/ip整理去重
* 使用mutli worker管理工人
* 子域名枚举增加字典枚举插件
* CDN检测
* ...
  
