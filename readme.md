## Src-Assert-Collection
* 收集SRC子域名资产，用于POC批量测试
* 利用Celery+Redis实现分布式任务，方便任务管理
* enumerate subdomains of websites using OSINT，使用[Sublist3r](https://github.com/aboul3la/Sublist3r)项目接口收集子域名

## Requirement
* 该项目目前仅在本地测试
* 本地安装celery+redis
* sublist3r依赖参照[Github](https://github.com/aboul3la/Sublist3r)

## Some Directory

Sublist3r默认设置

* other/备案domain.txt

  主域名列表

  * 运行other/get_src.py，other/getmaindomain.py更新
  * 或者手动添加

* data/subdomain

  收集到的子域名txt文件

* data/poc

  POC测试代码（目前可用CVE-2020-2551进行测试）

  

## Screenshots

收集子域名并实时监控，结果存放在/data/subdomain

* 开启redis服务

  ![标题](https://github.com/Dido1960/Src-Assert-Collection/blob/master/imgs/1.png)

* cd Get_Sub && python start.py 
  发布子域名收集任务并监控

  ![](https://github.com/Dido1960/Src-Assert-Collection/blob/master/imgs/2.png)

* 该项目借助sublist3r，可在tasks.py中设置其他引擎

  ![](https://github.com/Dido1960/Src-Assert-Collection/blob/master/imgs/3.png)



* 对收集的子域名列表进行POC测试（为了演示，这里本地搭建适用CVE-2020-2551[Weblogic环境](https://github.com/vulhub/vulhub/tree/master/weblogic/ssrf))，发现10.10.10.160可疑主机

![](https://github.com/Dido1960/Src-Assert-Collection/blob/master/imgs/4.png)
