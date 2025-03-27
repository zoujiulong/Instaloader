# Instaloader
How to use instaloader
## Install
`pip install instaloader`
## Common Question
Question1：**Error 401 - Unauthorized "fail" status**  
Solution:进入`instaloader`所在目录一般是`xxx\Lib\site-packages/instaloader`,打开`instaloadercontext.py`,搜索`def login(self, user, passwd):`,将`session.cookies.update({'sessionid': '', 'mid': '', 'ig_pr': '1',
                                'ig_vw': '1920', 'ig_cb': '1', 'csrftoken': '',
                                's_network': '', 'ds_user_id': ''})`中的`sessionid': ''`删除
## Use
官网<a href="https://github.com/instaloader/instaloader?tab=readme-ov-file" target="_">instaloader</a>，详细使用见<a href="https://instaloader.github.io/" target="_">文档</a>.  
使用`CLI`下载，你可以使用`instaloader TargetUsername --dirname-pattern TargetDir  --login Username --password Password`,`TargetUsername`为你想要下载的那个用户的用户名,`TargetDir`为下载到本地的目录，`Username`和`Passwrod`分别为你账号用户名和密码  
**注:CLI方法没有提供类似sleep的操作，直接运行容易被官网发现而封号**
使用`Python`下载，你可以下载`download.py`，并运行


