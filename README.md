# Instaloader
How to use instaloader
## Install
`pip install instaloader`
## Common Question
Question1：**Error 401 - Unauthorized "fail" status**  
Solution:进入`instaloader`所在目录一般是`xxx\Lib\site-packages/instaloader`,打开`instaloadercontext.py`,搜索`def login(self, user, passwd):`,将`session.cookies.update({'sessionid': '', 'mid': '', 'ig_pr': '1',
                                'ig_vw': '1920', 'ig_cb': '1', 'csrftoken': '',
                                's_network': '', 'ds_user_id': ''})`中的`sessionid': ''`删除.  
Question2:**Error 443**
Solution:多半因为没有开VPN或代理(科学上网).  
Question3:**Error 400 Bad Request - "fail" status**
Solution:我这里是因为爬虫数量较大将账号封了.
## Use
官网<a href="https://github.com/instaloader/instaloader?tab=readme-ov-file" target="_">instaloader</a>，详细使用见<a href="https://instaloader.github.io/" target="_">文档</a>.  
使用`CLI`下载，你可以使用`instaloader TargetUsername --dirname-pattern TargetDir  --login Username --password Password`,`TargetUsername`为你想要下载的那个用户的用户名,`TargetDir`为下载到本地的目录，`Username`和`Passwrod`分别为你账号用户名和密码.  

使用`Python`下载，下载`download.py`，在`CMD`中运行`instaloader --login username`,然后输入密码登录，运行`python download.py -username xx -targetUsername xx -saveDir xx -sleep xx`,`username`是自己账号用户名，`targetUsername`是目标用户名，`saveDir`是保存的本地目录，`sleep`是延迟爬虫间隔.  
**注:CLI方法没有提供类似sleep的操作，建议使用Python代码,每次爬取数量尽量不要太多，容易封号**
## Discussion
随着Facebook对调用类似Instagram API越来越严格，类似instaloader的库也要求必须使用账号登录，而每次脚本运行爬取部分post后都会被官方检测而导致封号，这里期待广大github热爱者来解决这个问题.


