* ## Src-Assert-Collection

  * 收集SRC子域名资产，用于POC批量测试
  * 利用Celery+Redis实现分布式任务，方便任务管理
  * enumerate subdomains of websites using OSINT，使用[Sublist3r](https://github.com/aboul3la/Sublist3r)项目接口收集子域名
  
  ## Requirement
  
  * 该项目目前仅在本地测试
  
  * 本地安装celery+redis
  
  * 项目依赖sublist3r，为了正确使用，我做了一点点[修改](https://github.com/Dido1960/Sublist3r)，请下载项目到根目录
  
    * 添加 \_\_init\_\_.py
  
    * 修改  from subbrute import subbrute  -> from Sublist3r.subbrute import subbrute
  
      最终的目录结构
  
      ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200528000857559.png)
  
  ## Some Directory
  
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
  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200527232053702.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODA5ODk2,size_16,color_FFFFFF,t_70)
  
  * cd Get_Sub && python start.py 
    发布子域名收集任务并监控
  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200527232053916.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODA5ODk2,size_16,color_FFFFFF,t_70)
  
  * 该项目借助sublist3r，可在tasks.py中设置其他引擎
  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200527232053817.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODA5ODk2,size_16,color_FFFFFF,t_70)
  
  * 对收集的子域名列表进行POC测试（为了演示，这里本地搭建适用CVE-2020-2551[Weblogic环境](https://github.com/vulhub/vulhub/tree/master/weblogic/ssrf))，发现10.10.10.160可疑主机
  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200527232053701.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODA5ODk2,size_16,color_FFFFFF,t_70)